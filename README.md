# Optimización de Rutas en Redes LAN mediante el Algoritmo de Dijkstra

## 📖 Descripción General
Este proyecto aborda el problema de la ineficiencia en la selección de rutas de transmisión en redes de área local (LAN). Mediante la aplicación de la Teoría de Grafos y el desarrollo desde cero del **algoritmo de Dijkstra**, el sistema simula una topología de red y calcula dinámicamente el árbol de caminos mínimos para reducir la latencia acumulada.

Proyecto desarrollado para la asignatura de **Matemática Avanzada** en la **Carrera de Tecnología de la Información**.

## ✨ Características Principales
* **Modelado Matemático:** Representación de dispositivos físicos (routers, switches, estaciones) como un grafo ponderado no dirigido.
* **Algoritmo de Dijkstra Propio:** Implementación computacional del algoritmo utilizando la técnica de relajación iterativa y colas de prioridad.
* **Eficiencia Computacional:** Uso de estructuras `min-heap` para alcanzar una complejidad temporal óptima de $O((V+E)\log V)$.
* **Simulación de Escenarios Dinámicos:** Evaluación de la red frente a variaciones de tráfico, congestión de enlaces y caída de nodos.
* **Validación Cruzada:** Comparación de los resultados empíricos frente a las métricas de la librería científica de referencia `NetworkX`.

## 🛠️ Tecnologías y Librerías Utilizadas
* **Lenguaje:** Python 3.x
* **Estructura de Datos:** `heapq` (para la gestión de la cola de prioridad)
* **Validación Científica:** `NetworkX` (análisis y validación de grafos)
* **Visualización:** `Matplotlib` (representación gráfica de la topología y rutas óptimas)

## ⚙️ Estructura del Proyecto
* `main.py`: Ejecución principal del algoritmo de Dijkstra y reconstrucción de la ruta óptima.
* `grafo_lan.py`: Definición de la topología de la red mediante diccionarios.
* `visualizacion.py`: Generación del entorno gráfico para el análisis visual de los enlaces.

## 🚀 Cómo ejecutarlo
1. Clona este repositorio: `git clone [URL_DE_TU_REPOSITORIO]`
2. Instala las dependencias necesarias: `pip install networkx matplotlib`
3. Ejecuta el archivo principal: `python main.py`
