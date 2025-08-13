import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.Graph()

grafo.add_nodes_from(range(1, 21))

arestas = [
    (1, 2, 4), (1, 3, 2), (2, 4, 5), (2, 5, 10),
    (3, 4, 3), (3, 6, 8), (4, 7, 4), (4, 8, 6),
    (5, 8, 2), (5, 9, 7), (6, 10, 1), (6, 11, 5),
    (7, 12, 3), (7, 13, 6), (8, 14, 4), (8, 15, 9),
    (9, 16, 8), (9, 17, 3), (10, 18, 7), (10, 19, 6),
    (11, 20, 2), (12, 15, 5), (13, 16, 4), (14, 17, 6),
    (15, 18, 2), (16, 19, 3), (17, 20, 7), (18, 19, 1),
    (19, 20, 2), (3, 9, 4), (2, 6, 6)
]

grafo.add_weighted_edges_from(arestas)

posicoes = nx.spring_layout(grafo, seed=42)
plt.figure(figsize=(12, 8))
nx.draw(grafo, posicoes, with_labels=True, node_size=700, node_color="lightblue", font_size=10)
rotulos = nx.get_edge_attributes(grafo, 'weight')
nx.draw_networkx_edge_labels(grafo, posicoes, edge_labels=rotulos)
plt.title("Grafo com 20 vértices e pesos")
plt.show()

caminho_minimo = nx.dijkstra_path(grafo, source=1, target=20, weight='weight')
distancia_minima = nx.dijkstra_path_length(grafo, source=1, target=20, weight='weight')

(caminho_minimo, distancia_minima)
