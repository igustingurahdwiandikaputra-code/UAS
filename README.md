# LAPORAN UJIAN AKHIR SEMESTER

# SISTEM PENDUKUNG KEPUTUSAN (DSS) REKOMENDASI RUMAH SAKIT DI BALI MENGGUNAKAN ALGORITMA GRAPH

---

# BAB I – PENDAHULUAN

## 1.1 Latar Belakang

Perkembangan teknologi informasi telah mendorong pemanfaatan sistem komputer dalam membantu proses pengambilan keputusan pada berbagai bidang, termasuk bidang kesehatan. Salah satu permasalahan yang sering dihadapi masyarakat adalah menentukan rumah sakit yang paling sesuai berdasarkan kebutuhan medis, lokasi, dan fasilitas yang tersedia.

Dalam kondisi tertentu, pasien membutuhkan informasi yang cepat mengenai rumah sakit yang memiliki spesialis sesuai dengan keluhan yang dialami. Selain itu, faktor jarak dan akses menuju rumah sakit juga menjadi pertimbangan penting.

Untuk mengatasi permasalahan tersebut, dibuat sebuah Sistem Pendukung Keputusan (Decision Support System/DSS) yang mampu memberikan rekomendasi rumah sakit terbaik di Bali dengan memanfaatkan struktur data graph dan algoritma pencarian jalur terpendek. Sistem ini menggunakan data rumah sakit, spesialisasi dokter, rating rumah sakit, serta hubungan antar lokasi untuk menghasilkan rekomendasi yang optimal.

---

## 1.2 Rumusan Masalah

Berdasarkan latar belakang di atas, rumusan masalah dalam penelitian ini adalah:

1. Bagaimana membangun sistem pendukung keputusan untuk rekomendasi rumah sakit di Bali?
2. Bagaimana menerapkan struktur data graph dalam pemodelan lokasi rumah sakit?
3. Bagaimana menggunakan algoritma graph untuk menentukan jalur terpendek menuju rumah sakit?
4. Bagaimana memberikan rekomendasi rumah sakit berdasarkan kebutuhan pasien?

---

## 1.3 Tujuan

Tujuan dari pembuatan sistem ini adalah:

1. Membangun aplikasi DSS rekomendasi rumah sakit berbasis Python.
2. Mengimplementasikan struktur data graph dalam representasi lokasi rumah sakit.
3. Mengimplementasikan algoritma Dijkstra untuk pencarian jalur terpendek.
4. Memberikan rekomendasi rumah sakit berdasarkan spesialis yang dibutuhkan pasien.

---

## 1.4 Manfaat

Manfaat yang diperoleh dari sistem ini adalah:

### Bagi Pengguna

* Membantu menemukan rumah sakit yang sesuai dengan kebutuhan.
* Menghemat waktu dalam mencari layanan kesehatan.

### Bagi Akademik

* Sebagai implementasi nyata struktur data graph.
* Sebagai penerapan konsep DSS dalam bidang kesehatan.

### Bagi Pengembang

* Menambah pengalaman dalam pengembangan aplikasi berbasis data dan graph.

---

# BAB II – DASAR TEORI

## 2.1 Struktur Data Graph

Graph merupakan struktur data yang terdiri dari kumpulan simpul (vertex/node) dan hubungan antar simpul (edge).

Secara matematis graph dapat dituliskan:

G = (V, E)

Keterangan:

* V = himpunan vertex/node
* E = himpunan edge

Pada sistem ini:

* Node merepresentasikan lokasi dan rumah sakit.
* Edge merepresentasikan hubungan atau jalur antar lokasi.

---

## 2.2 Decision Support System (DSS)

Decision Support System (DSS) adalah sistem informasi yang digunakan untuk membantu proses pengambilan keputusan dengan memanfaatkan data, model, dan metode analisis.

Karakteristik DSS:

* Mendukung keputusan semi-terstruktur.
* Memanfaatkan data dan model analisis.
* Memberikan alternatif solusi terbaik.

Pada sistem ini DSS digunakan untuk menentukan rumah sakit yang paling sesuai berdasarkan:

* Keluhan pasien
* Jarak
* Rating rumah sakit
* Ketersediaan spesialis

---

## 2.3 Algoritma Graph yang Digunakan

### Algoritma Dijkstra

Algoritma Dijkstra digunakan untuk menentukan jalur terpendek dari satu node ke node lain pada graph berbobot.

Langkah kerja:

1. Tentukan node awal.
2. Beri nilai 0 pada node awal dan tak hingga pada node lain.
3. Pilih node dengan jarak minimum.
4. Perbarui jarak tetangga.
5. Ulangi hingga mencapai node tujuan.

Keunggulan:

* Efisien untuk graph berbobot positif.
* Menjamin solusi optimal.

---

### Degree Centrality

Degree Centrality digunakan untuk mengetahui tingkat keterhubungan suatu node.

Rumus:

CD(v) = deg(v) / (n − 1)

Semakin besar nilainya maka semakin penting posisi node tersebut dalam graph.

---

# BAB III – ANALISIS DAN PERANCANGAN

## 3.1 Analisis Masalah

Masalah utama yang dihadapi pengguna adalah menentukan rumah sakit yang sesuai dengan kondisi pasien dan memiliki akses tercepat dari lokasi pengguna.

Solusi yang dirancang adalah sistem yang:

1. Menerima input keluhan pengguna.
2. Menentukan spesialis yang dibutuhkan.
3. Menyeleksi rumah sakit yang memiliki spesialis tersebut.
4. Menghitung rekomendasi berdasarkan rating dan jarak.
5. Menampilkan jalur terpendek menuju rumah sakit.

---

## 3.2 Desain Graph

Representasi graph:

Node:

* Lokasi pengguna
* Rumah sakit

Edge:

* Jalur antar lokasi
* Bobot berupa jarak

Contoh:

Lokasi A → RSUP Sanglah = 5 km

Lokasi A → RS BaliMed = 8 km

Lokasi A → RS Kasih Ibu = 6 km

---

## 3.3 Flowchart

Alur sistem:

Start

↓

Input Keluhan

↓

Tentukan Spesialis

↓

Cari Rumah Sakit Sesuai

↓

Hitung Skor Rekomendasi

↓

Hitung Jalur Terpendek (Dijkstra)

↓

Tampilkan Hasil

↓

End

---

## 3.4 Use Case

### Aktor

Pengguna

### Use Case

1. Memasukkan keluhan.
2. Memilih lokasi awal.
3. Melihat rekomendasi rumah sakit.
4. Melihat rute terpendek.
5. Melihat analisis graph.

---

## 3.5 Struktur Node dan Edge

### Node

| Node             | Keterangan      |
| ---------------- | --------------- |
| User             | Lokasi pengguna |
| RSUP Sanglah     | Rumah sakit     |
| RS BaliMed       | Rumah sakit     |
| RS Kasih Ibu     | Rumah sakit     |
| RS Surya Husadha | Rumah sakit     |

### Edge

| Asal | Tujuan           | Bobot |
| ---- | ---------------- | ----- |
| User | RSUP Sanglah     | Jarak |
| User | RS BaliMed       | Jarak |
| User | RS Kasih Ibu     | Jarak |
| User | RS Surya Husadha | Jarak |

---

# BAB IV – IMPLEMENTASI

## 4.1 Implementasi Program

Program dikembangkan menggunakan:

* Python
* Streamlit
* NetworkX
* Pandas
* Folium

Modul utama:

* app.py
* dijkstra.py
* graph_data.py
* ai_recommendation.py
* centrality.py

---

## 4.2 Penjelasan Kode

### Modul Dijkstra

Fungsi:

* Menghitung jalur terpendek.
* Menentukan total jarak minimum.

Output:

* Jalur terbaik.
* Total biaya/jarak.

---

### Modul Recommendation

Fungsi:

* Mengubah keluhan menjadi spesialis.

Contoh:

Nyeri Dada → Jantung

Sesak Nafas → Paru

---

### Modul Centrality

Fungsi:

* Menghitung degree centrality setiap node.

Tujuan:

* Mengetahui node yang paling strategis dalam jaringan.

---

## 4.3 Tampilan Sistem

Tampilan aplikasi terdiri dari:

1. Halaman input keluhan.
2. Halaman rekomendasi rumah sakit.
3. Visualisasi peta rumah sakit.
4. Analisis graph.
5. Jalur terpendek menggunakan Dijkstra.

(Sisipkan screenshot aplikasi pada bagian ini.)

---

# BAB V – PENGUJIAN DAN ANALISIS

## 5.1 Skenario Pengujian

### Pengujian 1

Input:

Keluhan = Nyeri Dada

Output yang diharapkan:

Rumah sakit dengan spesialis jantung muncul sebagai rekomendasi.

Status:

Berhasil.

---

### Pengujian 2

Input:

Lokasi pengguna → RSUP Sanglah

Output:

Jalur terpendek berhasil dihitung.

Status:

Berhasil.

---

## 5.2 Analisis Hasil

Hasil pengujian menunjukkan bahwa:

* Sistem mampu memfilter rumah sakit berdasarkan spesialis.
* Algoritma Dijkstra berhasil menentukan jalur minimum.
* Degree Centrality berhasil mengidentifikasi node penting dalam graph.
* Dashboard dapat menampilkan hasil secara interaktif.

---

## 5.3 Kompleksitas Algoritma

### Dijkstra

Kompleksitas waktu:

O((V + E) log V)

Keterangan:

* V = jumlah node
* E = jumlah edge

### Degree Centrality

Kompleksitas waktu:

O(V + E)

Karena setiap node dan edge dihitung satu kali.

---

# BAB VI – KESIMPULAN

## 6.1 Kesimpulan

Berdasarkan hasil implementasi dan pengujian, dapat disimpulkan bahwa:

1. Sistem pendukung keputusan berhasil dibangun menggunakan Python dan Streamlit.
2. Struktur data graph mampu merepresentasikan hubungan antar lokasi dan rumah sakit.
3. Algoritma Dijkstra berhasil menentukan jalur terpendek menuju rumah sakit.
4. Sistem dapat memberikan rekomendasi rumah sakit sesuai kebutuhan pasien.
5. Visualisasi graph dan peta membantu pengguna memahami hasil rekomendasi dengan lebih baik.

---

## 6.2 Saran Pengembangan

Beberapa pengembangan yang dapat dilakukan pada penelitian selanjutnya:

1. Menambahkan data rumah sakit yang lebih lengkap.
2. Mengintegrasikan GPS secara real-time.
3. Menambahkan algoritma Multi Criteria Decision Making (MCDM).
4. Menggunakan data lalu lintas aktual untuk perhitungan rute.
5. Mengembangkan aplikasi ke platform mobile Android dan iOS.

---
