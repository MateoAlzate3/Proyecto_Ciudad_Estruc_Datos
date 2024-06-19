# city_graph.py
import networkx as nx


def create_city_graph():
    G = nx.Graph()
    # Agregar nodos (ubicaciones) con coordenadas para pygame
    G.add_node(1, pos=(50, 50), type='house')
    G.add_node(2, pos=(150, 50), type='park')
    G.add_node(3, pos=(250, 50), type='supermarket')
    G.add_node(4, pos=(350, 50), type='house')
    G.add_node(5, pos=(50, 150), type='church')
    G.add_node(6, pos=(150, 150), type='house')
    G.add_node(7, pos=(250, 150), type='house')
    G.add_node(8, pos=(350, 150), type='house')
    G.add_node(9, pos=(50, 250), type='house')
    G.add_node(10, pos=(150, 250), type='park')
    G.add_node(11, pos=(250, 250), type='supermarket')
    G.add_node(12, pos=(350, 250), type='house')
    G.add_node(13, pos=(50, 350), type='house')
    G.add_node(14, pos=(150, 350), type='church')
    G.add_node(15, pos=(250, 350), type='house')
    G.add_node(16, pos=(350, 350), type='house')

    # Agregar aristas (caminos) con distancias
    edges = [
        (1, 2, 1), (2, 3, 1), (3, 4, 1),
        (5, 6, 1), (6, 7, 1), (7, 8, 1),
        (9, 10, 1), (10, 11, 1), (11, 12, 1),
        (13, 14, 1), (14, 15, 1), (15, 16, 1),
        (1, 5, 1), (5, 9, 1), (9, 13, 1),
        (2, 6, 1), (6, 10, 1), (10, 14, 1),
        (3, 7, 1), (7, 11, 1), (11, 15, 1),
        (4, 8, 1), (8, 12, 1), (12, 16, 1),
    ]

    G.add_weighted_edges_from(edges)

    return G


if __name__ == "__main__":
    city_graph = create_city_graph()
    pos = nx.get_node_attributes(city_graph, 'pos')
    print(pos)
