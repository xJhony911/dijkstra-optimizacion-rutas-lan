# ====================================================
# main.py
# Implementación del algoritmo de Dijkstra
# ====================================================
 
import heapq

from grafo_lan import grafo


def dijkstra(grafo, origen):

    # Inicialización:
    # d(v)=∞ para todos los vértices

    distancias = {
        nodo: float('inf')
        for nodo in grafo
    }

    # π(v)=NIL

    predecesores = {
        nodo: None
        for nodo in grafo
    }

    # Distancia del origen

    distancias[origen] = 0

    cola = [(0, origen)]

    while cola:

        distancia_actual, actual = heapq.heappop(cola)

        for vecino, peso in grafo[actual].items():

            # Relajación:
            # d(v) > d(u)+w(u,v)

            nueva_distancia = (
                distancia_actual + peso
            )

            if nueva_distancia < distancias[vecino]:

                distancias[vecino] = nueva_distancia

                predecesores[vecino] = actual

                heapq.heappush(
                    cola,
                    (nueva_distancia, vecino)
                )

    return distancias, predecesores


def reconstruir_ruta(
        predecesores,
        destino
):

    ruta = []

    while destino:

        ruta.append(destino)

        destino = predecesores[destino]

    ruta.reverse()

    return ruta

# =============================
# Programa principal
# =============================

origen = 'A'
destino = 'H'

distancias, predecesores = dijkstra(
    grafo,
    origen
)

ruta = reconstruir_ruta(
    predecesores,
    destino
)

print("=" * 50)

print("ALGORITMO DE DIJKSTRA")

print("=" * 50)

print(f"Origen : {origen}")

print(f"Destino: {destino}")

print()

print("Ruta óptima:")

print(" -> ".join(ruta))

print()

print(
    f"Costo total: "
    f"{distancias[destino]}"
)

print("=" * 50)
