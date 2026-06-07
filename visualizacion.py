# visualizacion.py
# Visualización de la topología LAN
# ====================================================

 
import networkx as nx

import matplotlib.pyplot as plt

from grafo_lan import grafo


G = nx.Graph()

for nodo in grafo:

    for vecino, peso in grafo[nodo].items():

        G.add_edge(
            nodo,
            vecino,
            weight=peso
        )

pos = nx.spring_layout(
    G,
    seed=42
)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500
)

etiquetas = nx.get_edge_attributes(
    G,
    'weight'
)

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=etiquetas
)

plt.title(
    "Topología LAN del Proyecto"
)

plt.show()
 

