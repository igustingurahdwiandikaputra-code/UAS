
# UAS PREMIUM - DSS RUMAH SAKIT BALI
import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import folium

from folium.plugins import MarkerCluster, Fullscreen, MiniMap, MeasureControl
from streamlit_folium import st_folium

from graph_data import build_graph
from dijkstra import dijkstra
from centrality import calculate_centrality
from ai_recommendation import get_specialist

st.set_page_config(
    page_title="DSS Rumah Sakit Bali Premium",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
<style>
.stApp{background:#1a2332;}
.header-top{
background:linear-gradient(135deg,#355872,#7AAACE);
padding:20px;border-radius:15px;color:white;margin-bottom:15px;
}
.section-title{
font-size:1.2rem;font-weight:bold;color:#9CD5FF;margin:15px 0;
}
.card{
background:#2a3a4e;
padding:15px;
border-radius:12px;
border:1px solid #3a4a5e;
margin-bottom:10px;
color:white;
}
.stats-row{
display:grid;
grid-template-columns:repeat(4,1fr);
gap:15px;
}
.stat-card{
background:#2a3a4e;
padding:18px;
border-radius:12px;
text-align:center;
border:1px solid #3a4a5e;
}
.stat-title{color:#9CD5FF;}
.stat-value{font-size:24px;font-weight:bold;color:white;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-top">
<h1>🏥 DSS Rekomendasi Rumah Sakit Bali</h1>
<p>Decision Support System menggunakan Dijkstra, Centrality, dan Analisis Spesialis</p>
</div>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return build_graph()

graph, df = load_data()

with st.sidebar:

    st.header("⚙️ Preferensi Pasien")

    keluhan = st.selectbox(
        "Keluhan",
        ["Nyeri Dada","Sesak Nafas","Cedera","Sakit Kepala"]
    )

    lokasi_awal = st.selectbox(
        "📍 Lokasi Awal",
        [
            "Denpasar",
            "Kuta",
            "Sanur",
            "Ubud",
            "Jimbaran",
            "Nusa Dua"
        ]
    )

    zoom = st.slider(
        "Zoom Peta",
        8,
        16,
        11
    )

    tampil_graph = st.checkbox(
        "Tampilkan Graph",
        False
    )

    tampil_centrality = st.checkbox(
        "Tampilkan Centrality",
        True
    )

    cari = st.button(
        "🔍 Cari Rute Terbaik",
        use_container_width=True
    )

lokasi_coords = {
    "Denpasar": (-8.6705, 115.2126),
    "Kuta": (-8.7220, 115.1710),
    "Sanur": (-8.6940, 115.2630),
    "Ubud": (-8.5060, 115.2620),
    "Jimbaran": (-8.7900, 115.1600),
    "Nusa Dua": (-8.8080, 115.2300)
}
spesialis = get_specialist(keluhan)

st.success(f"🎯 Spesialis yang direkomendasikan: {spesialis}")

ranking = []

for _, row in df.iterrows():

    spesialis_rs = [
        s.strip()
        for s in str(row["Spesialis"]).split(",")
    ]

    if spesialis in spesialis_rs:

        score = (row["Rating"] * 10) - row["Jarak"]

        ranking.append(
            (
                row["RumahSakit"],
                score,
                row["Rating"],
                row["Jarak"]
            )
        )

ranking.sort(key=lambda x: x[1], reverse=True)

best_rs = ranking[0][0] if ranking else None

info_col, map_col = st.columns([1,3])

with info_col:

    st.markdown("### 🏆 Top 3 Rumah Sakit")

    for i, rs in enumerate(ranking[:3]):
        st.markdown(f"""
        <div class='card'>
        <b>#{i+1} {rs[0]}</b><br>
        Rating: {rs[2]} ⭐<br>
        Jarak: {rs[3]} KM<br>
        Skor: {rs[1]:.2f}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📋 Informasi")
    st.write("Lokasi Pasien :", lokasi_awal)
    st.write("Keluhan :", keluhan)
    st.write("Spesialis :", spesialis)

    cost = 0
    path = []

    if best_rs:
        st.write("Rekomendasi Utama :", best_rs)

with map_col:

    center_lat = df["Latitude"].mean()
    center_lon = df["Longitude"].mean()

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=zoom,
        control_scale=True
    )

    Fullscreen().add_to(m)
    MiniMap().add_to(m)
    MeasureControl().add_to(m)

    cluster = MarkerCluster().add_to(m)

    coords = {}

    for _, row in df.iterrows():

        coords[row["RumahSakit"]] = (
            row["Latitude"],
            row["Longitude"]
        )

        warna = "red"

        if row["RumahSakit"] != best_rs:
            warna = "blue"

        folium.Marker(
            [row["Latitude"], row["Longitude"]],
            tooltip=row["RumahSakit"],
            popup=f"""
            <b>{row['RumahSakit']}</b><br>
            Spesialis : {row['Spesialis']}<br>
            Rating : {row['Rating']}<br>
            Fasilitas : {row['Fasilitas']}
            """,
            icon=folium.Icon(color=warna, icon="plus")
        ).add_to(cluster)
        # Marker lokasi pasien
    folium.Marker(
        lokasi_coords[lokasi_awal],
        tooltip="Lokasi Pasien",
        popup=f"Lokasi Awal: {lokasi_awal}",
        icon=folium.Icon(
        color="green",
        icon="home"
        )
    ).add_to(m)

# Garis lokasi pasien ke RS rekomendasi
if best_rs:

    rs_data = df[
        df["RumahSakit"] == best_rs
    ].iloc[0]

    folium.PolyLine(
        [
            lokasi_coords[lokasi_awal],
            (
                rs_data["Latitude"],
                rs_data["Longitude"]
            )
        ],
        color="green",
        weight=5,
        tooltip="Rute Pasien ke RS"
    ).add_to(m)

route = []

if cari and lokasi_awal and best_rs:

        cost, path = dijkstra(
            graph,
            lokasi_awal,
            best_rs
        )

        route = [lokasi_coords[lokasi_awal]]

        for rs in path:
            if rs in coords:
                route.append(coords[rs])

if len(route) > 1:
            folium.PolyLine(
                route,
                color="red",
                weight=6,
                opacity=0.8,
                tooltip="Rute Dijkstra"
            ).add_to(m)

st_folium(
    m,
    width=1100,
    height=650
)

if cari and best_rs and path:

    st.markdown(
        f"### 🏥 Rumah Sakit Terbaik\n{best_rs}"
    )

    rs_data = df[
        df["RumahSakit"] == best_rs
    ].iloc[0]

    st.metric(
        "Rating",
        rs_data["Rating"]
    )

    st.metric(
        "Jarak",
        f"{rs_data['Jarak']} KM"
    )

    st.markdown(
        f"### 🛣️ Rute Terbaik\n{' ➜ '.join(path)}"
    )

    estimasi = round(cost * 2)

    st.markdown(f"""
    <div class="stats-row">

        <div class="stat-card">
            <div class="stat-title">Jarak</div>
            <div class="stat-value">{cost} KM</div>
        </div>

        <div class="stat-card">
            <div class="stat-title">Estimasi</div>
            <div class="stat-value">{estimasi} Menit</div>
        </div>

        <div class="stat-card">
            <div class="stat-title">Node</div>
            <div class="stat-value">{len(path)}</div>
        </div>

        <div class="stat-card">
            <div class="stat-title">RS Terbaik</div>
            <div class="stat-value">{best_rs}</div>
        </div>

    </div>
    """, unsafe_allow_html=True)

    detail = []

    for i in range(len(path)-1):

        detail.append([
        i+1,
        path[i],
        path[i+1],
        graph.get(path[i], {}).get(path[i+1], 0)
    ])

    st.markdown("### 📋 Detail Rute")

    st.dataframe(
        pd.DataFrame(
            detail,
            columns=[
                "No",
                "Dari",
                "Ke",
                "Jarak (KM)"
            ]
        ),
        use_container_width=True
    )

if tampil_centrality:

    st.markdown("### 📈 Degree Centrality")

    centrality = calculate_centrality(graph)

    centrality_df = pd.DataFrame(
        centrality.items(),
        columns=["Rumah Sakit","Centrality"]
    ).sort_values(
        "Centrality",
        ascending=False
    )

    st.dataframe(
        centrality_df,
        use_container_width=True
    )

if tampil_graph:

    st.markdown("### 🔗 Visualisasi Graph")

@st.cache_resource
def build_network_graph(graph):

    G = nx.Graph()

    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(
                node,
                neighbor,
                weight=weight
            )

    return G

if tampil_graph:

    G = build_network_graph(graph)

    fig, ax = plt.subplots(figsize=(12,7))

    pos = nx.spring_layout(
        G,
        seed=42
    )

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=3500,
        node_color="skyblue",
        font_weight="bold",
        ax=ax
    )

    labels = nx.get_edge_attributes(G,"weight")

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=labels
    )

    st.pyplot(fig)

st.markdown("### 🏥 Data Rumah Sakit")
st.dataframe(df, use_container_width=True)
