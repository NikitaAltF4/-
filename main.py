import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue


def visualize_graph(graph, colors):
    # Отображение графа с метками и раскраской вершин
    nx.draw(graph, with_labels=True, node_color=[colors.get(node, 'White') for node in graph.nodes()])
    plt.show()


def breadth_first_search(graph, start):
    visited = {}  # Словарь для отслеживания посещенных вершин
    colors = {}  # Словарь для отслеживания раскраски вершин

    # Инициализация словарей visited и colors
    for vertex in graph:
        visited[vertex] = False
        colors[vertex] = None

    visited[start] = True
    colors[start] = 'Red'

    queue = Queue()  # Очередь для обхода в ширину
    queue.put(start)

    while not queue.empty():
        current_vertex = queue.get()

        adjacent_vertices = list(graph.neighbors(current_vertex))#получает список смежных вершин

        for vertex in adjacent_vertices:
            if not visited[vertex]:
                visited[vertex] = True

                available_colors = {'Red', 'Green', 'Blue', 'Black', 'Yellow', 'Purple', 'brown', 'gray'}
                # Проверка доступных цветов у соседних вершин
                for adjacent_vertex in graph.neighbors(vertex):
                    if colors[adjacent_vertex] in available_colors:
                        available_colors.remove(colors[adjacent_vertex])

                colors[vertex] = available_colors.pop()  # Присвоение вершине доступного цвета
                queue.put(vertex)

    return colors


# Создание пустого графа
graph = nx.Graph()

# Ввод вершин графа
vertices = input("Введите вершины графа (через запятую): ").replace(" ", "").split(",")
graph.add_nodes_from(vertices)

# Ввод ребер графа
print("Введите ребра графа (в формате 'вершина1,вершина2', для завершения введите 'q'):")
while True:
    edge = input()
    if edge == "q":
        break
    else:
        u, v = edge.replace(" ", "").split(",")
        graph.add_edge(u, v)

# Отображение исходного графа
visualize_graph(graph, {})

# Выбор начальной вершины
start_vertex = input("Выберите начальную вершину:")

# Выполнение обхода в ширину и раскраска вершин
colored_vertices = breadth_first_search(graph, start_vertex)

# Отображение раскрашенного графа
nx.set_node_attributes(graph, colored_vertices, 'color')
visualize_graph(graph, colored_vertices)
