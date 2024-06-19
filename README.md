Manual de Usuario - Simulación de Taxis

Bienvenido al manual de usuario para la simulación de taxis en una ciudad utilizando el algoritmo de Dijkstra. Este manual te guiará a través de los pasos necesarios para ejecutar y utilizar el programa de manera efectiva.
Requisitos Previos
Para poder ejecutar la simulación, asegúrate de tener instalado lo siguiente en tu sistema:
	Python: Debe estar instalado Python 3.6 en adelante. Puedes descargarlo desde python.org.
	Pygame: La simulación utiliza Pygame para la interfaz gráfica. Puedes instalarlo usando pip si no lo tienes instalado:
                                              pip install pygame     (esto se hace en la consola)
Ejecución del Programa
Sigue estos pasos para ejecutar la simulación:
Descargar el Código Fuente:
Descarga o clona el repositorio desde GitHub donde se encuentra el código fuente de la simulación.
                  https://github.com/MateoAlzate3/Proyecto_Ciudad_Estruc_Datos
Ejecutar el Programa:
1.	Abre una terminal o línea de comandos.
2.	Navega al directorio donde has descargado el código fuente de la simulación.
3.	Ejecutar el Script Principal:
4.	Ejecuta el archivo main.py usando Python:
                                               python main.py        (esto se hace en la consola)
5.	Esto iniciará la simulación y abrirá una ventana de interfaz gráfica.

Interfaz de Usuario
Una vez que la simulación esté en ejecución, interactúa con la interfaz de usuario para añadir taxis, pasajeros y ejecutar la simulación:
Añadir Taxis:
	Utiliza los botones etiquetados como "Recoger en X" para añadir taxis en diferentes ubicaciones de la ciudad.
	Recoger en A
	Recoger en B
	Recoger en C
	Haz clic en uno de estos botones para seleccionar el punto de recogida del pasajero.

Añadir Pasajeros:
	Utiliza los botones etiquetados como "Destino X" para añadir pasajeros con ubicaciones de recogida y destinos específicos.
	llevar B
	llevar A
	llevar C
	Haz clic en uno de estos botones para seleccionar el punto de destino del pasajero.

Ejecutar la Simulación:
	Una vez añadidos taxis y pasajeros, la simulación comenzará automáticamente. Los taxis se moverán para recoger a los pasajeros y llevarlos a sus destinos utilizando el algoritmo de Dijkstra.
Visualización
	Los taxis y pasajeros se representarán en el mapa:
	Los taxis se mostrarán como imágenes de taxi.png.
	Los pasajeros se mostrarán como imágenes de passenger.png en su punto de recogida.
	A medida que los taxis se muevan, verás sus posiciones actualizándose en el mapa.

Finalización del Programa
Cerrar la Simulación:
Para cerrar la simulación, simplemente cierra la ventana de interfaz gráfica. Esto detendrá la ejecución del programa.
Notas Adicionales
	Asegúrate de tener una conexión estable a Internet al ejecutar la simulación por primera vez, ya que algunos recursos gráficos como imágenes de fondo pueden necesitar ser descargados o estar disponibles localmente en la carpeta src.
	El programa está diseñado para ser intuitivo, pero si encuentras algún problema o tienes preguntas adicionales, revisa la documentación proporcionada o consulta con el desarrollador del proyecto.


Descripción del Problema y Objetivo del Proyecto
El objetivo de este proyecto es desarrollar una simulación gráfica que represente el funcionamiento de un sistema de taxis en una ciudad. En la simulación, los taxis deben recoger pasajeros en puntos específicos y llevarlos a sus destinos. Este proyecto tiene como finalidad demostrar el uso de estructuras de datos (grafos) y algoritmos (Dijkstra) para solucionar problemas de rutas y navegación en un entorno urbano.
Modelado de la Ciudad como un Grafo
La ciudad se modela como un grafo no dirigido donde:
Nodos: Representan ubicaciones específicas de la ciudad, como calles o intersecciones.
Aristas: Representan las calles que conectan estas ubicaciones, con un peso asociado que puede indicar la distancia o el tiempo de viaje entre dos nodos.
En la implementación, se define un diccionario ‘aristas’ para almacenar las conexiones entre nodos, y un conjunto ‘nodos’ para almacenar todas las ubicaciones. Cada arista tiene un peso que representa la distancia entre los nodos conectados.

Algoritmo de Dijkstra y su Implementación
El algoritmo de Dijkstra se utiliza para encontrar la ruta más corta entre dos nodos en un grafo con pesos no negativos. El proceso es el siguiente:
Inicialización: Se establece una cola de prioridad con la distancia inicial de 0 desde el nodo de inicio. Las distancias a todos los demás nodos se inicializan a infinito.
Exploración de Nodos: Se extrae el nodo con la distancia más pequeña de la cola de prioridad y se actualizan las distancias a sus vecinos si se encuentra una ruta más corta.
Actualización de Caminos: Se sigue este proceso hasta que todos los nodos han sido procesados o se ha encontrado la distancia más corta al nodo de destino.
En el código, la implementación del algoritmo de Dijkstra se realiza mediante una función que utiliza una cola de prioridad (‘heapq’) para gestionar eficientemente las distancias mínimas. La función devuelve la ruta más corta y la distancia total.

Modelo de Taxis y Pasajeros y Lógica de Recogida y Entrega
Taxis:
Cada taxi se representa mediante una clase ‘Taxi’ que incluye:
Atributos: Identificador, ubicación actual, destino, estado de ocupación, ruta actual, velocidad, y estado de movimiento.
Métodos: Para asignar destinos, calcular rutas utilizando Dijkstra, y mover el taxi a lo largo de su ruta.
Pasajeros:
Cada pasajero se representa mediante una clase Pasajero con atributos como identificador, ubicación inicial, ubicación de destino, y estado de recogida.
Lógica de Recogida y Entrega
Asignación de Pasajeros: Cuando se crea un pasajero, se encuentra el taxi más cercano disponible utilizando una función que calcula la distancia euclidiana entre la ubicación del taxi y la del pasajero. El taxi más cercano se asigna para recoger al pasajero.
Movimiento del Taxi: El taxi se mueve hacia la ubicación del pasajero, lo recoge y luego lo lleva a su destino. Una vez que el pasajero es dejado en su destino, el taxi regresa a su punto de partida o espera nuevas instrucciones.
Análisis de Resultados y Posibles Mejoras Futuras
Resultados:
El proyecto demuestra exitosamente la simulación de un sistema de taxis en una ciudad modelada como un grafo. Los taxis pueden recoger pasajeros y transportarlos a sus destinos, utilizando rutas óptimas calculadas por el algoritmo de Dijkstra. La simulación gráfica permite visualizar el movimiento de los taxis y la interacción con los pasajeros.
Posibles Mejoras Futuras
Optimización de Algoritmo: Implementar algoritmos más avanzados como A* para mejorar la eficiencia de la búsqueda de rutas.
Modelado de Tráfico: Introducir variaciones en los pesos de las aristas para simular condiciones de tráfico en tiempo real.
Interfaz de Usuario Mejorada: Añadir más controles y visualizaciones para mejorar la interacción del usuario con la simulación.
Ampliación del Grafo: Modelar una ciudad más grande y compleja con más nodos y aristas para una simulación más realista.
Inteligencia Artificial: Incorporar técnicas de IA para la toma de decisiones de los taxis en situaciones complejas.
