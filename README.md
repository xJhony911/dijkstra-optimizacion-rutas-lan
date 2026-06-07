## 👨‍💻 Equipo de Desarrollo

Este proyecto fue desarrollado de forma colaborativa por estudiantes de cuarto semestre (PAO 4) de la carrera de **Tecnología de la Información** en la **ESPOCH**, uniendo bases de matemática avanzada con programación en Python.

| Integrante | Rol | Enfoque Principal |
| :--- | :--- | :--- |
| **Jonathan Acosta** 👑 | Líder del Proyecto | Coordinación general, arquitectura de la solución y dirección técnica del desarrollo. |
| **Dennys Daquilema** 🧮 | Desarrollo Matemático | Modelado teórico del grafo, demostración de la técnica de relajación y matrices.|
| **Jhonn Elizalde** 💻 | Impl. Computacional | Traducción de la matemática a código, manejo de la cola de prioridad (`heapq`). |
| **José Mullo** 🕵️‍♂️ | Validación | Pruebas de estrés, simulación de escenarios dinámicos y validación cruzada.[cite: 1] |
| **Kevin Chinlle** 📝 | Documentación | Estructuración metodológica, redacción técnica y rigor académico. |
| **Kevin Morales** 🎨 | Presentación | Diseño visual, diagramación de la topología y comunicación de resultados.|

# Optimización de Rutas en Redes LAN mediante el Algoritmo de Dijkstra

## 📖 Descripción General
Este proyecto aborda el problema de la ineficiencia en la selección de rutas de transmisión en redes de área local (LAN). Mediante la aplicación de la Teoría de Grafos y el desarrollo desde cero del **algoritmo de Dijkstra**, el sistema simula una topología de red y calcula dinámicamente el árbol de caminos mínimos para reducir la latencia acumulada.

Proyecto desarrollado para la asignatura de **Matemática Avanzada** en la **Carrera de Tecnología de la Información**.

## 🧠 ¿Qué es el Algoritmo de Dijkstra?

El algoritmo de Dijkstra es un método voraz (*greedy*) diseñado para resolver el problema del camino mínimo en grafos ponderados con pesos no negativos. Su objetivo es determinar con exactitud la ruta de menor costo acumulado desde un nodo origen hacia todos los demás nodos que componen la red.

### ¿Cómo funciona matemáticamente?
El algoritmo se basa en la **técnica de relajación** iterativa. Mantiene estructuras de datos para rastrear las distancias mínimas conocidas y los nodos predecesores. En cada paso, selecciona el vértice con el costo acumulado más bajo y evalúa a todos sus vecinos. Si descubre que pasar por ese vértice ofrece un camino más "barato" hacia un vecino, actualiza la distancia mínima de ese vecino (relajación). 

Para que este proceso sea computacionalmente eficiente, nuestro proyecto implementa una cola de prioridad basada en `min-heap` (mediante la librería `heapq` de Python), logrando una complejidad temporal óptima de **$O((V+E)\log V)$**.

### Su aplicación en este proyecto (Redes LAN)
En el ámbito de la Tecnología de la Información, Dijkstra es la base matemática fundamental de protocolos de enrutamiento dinámico de estado de enlace (Link-State) utilizados en la industria, como **OSPF** (Open Shortest Path First). 

En nuestro modelo de simulación:
* **Los vértices (V)** representan los dispositivos físicos de la LAN (routers, switches, estaciones de trabajo).
* **Las aristas (E)** representan los enlaces de comunicación.
* **El peso (w)** de cada enlace representa la **latencia medida en milisegundos (ms)**. 

Por lo tanto, al calcular el "camino mínimo", el algoritmo está identificando activamente la ruta más rápida y eficiente para la transmisión de paquetes de datos, evitando cuellos de botella y maximizando el rendimiento de la red.
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
## ☁️ Prueba Rápida en la Nube (Google Colab)

Si deseas probar la simulación, ver el código en acción y explorar la visualización gráfica de la red sin necesidad de instalar Python ni clonar el repositorio localmente, hemos preparado un entorno interactivo.

Puedes ejecutar todo el proyecto directamente en tu navegador haciendo clic en el siguiente botón:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1o3w4UHJfTHMeLBkFKAgm5gWISPbSu9CS?usp=sharing)

**Instrucciones para Colab:**
1. Abre el enlace.
2. Inicia sesión con tu cuenta de Google.
3. Ve a la pestaña **Entorno de ejecución** y selecciona **Ejecutar todo** (o presiona `Ctrl + F9`).
## ⚙️ Estructura del Proyecto
* `main.py`: Ejecución principal del algoritmo de Dijkstra y reconstrucción de la ruta óptima.
* `grafo_lan.py`: Definición de la topología de la red mediante diccionarios.
* `visualizacion.py`: Generación del entorno gráfico para el análisis visual de los enlaces.

## 🚀 Cómo ejecutarlo
1. Clona este repositorio: `git clone [URL_DE_TU_REPOSITORIO]`
2. Instala las dependencias necesarias: `pip install networkx matplotlib`
3. Ejecuta el archivo principal: `python main.py`
