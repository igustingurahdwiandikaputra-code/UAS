import networkx as nx

def calculate_centrality(graph):

    G = nx.Graph()

    for node in graph:

        for neighbor, weight in graph[node].items():

            G.add_edge(
                node,
                neighbor,
                weight=weight
            )

    return nx.degree_centrality(G)
