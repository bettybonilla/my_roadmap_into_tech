"""
The below represents a graph in code
"""

from typing import Any


class Graph:
    # Initializer AKA constructor
    def __init__(self):
        self.adj_list = {}

    # Adds a vertex in the Graph object
    def add_vertex(self, vertex: Any) -> bool:
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    # Removes a vertex in the Graph object
    def remove_vertex(self, vertex: Any) -> bool:
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    # Adds a bidirectional edge in the Graph object
    def add_edge(self, v1: Any, v2: Any) -> bool:
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    # Removes a bidirectional edge in the Graph object
    def remove_edge(self, v1: Any, v2: Any) -> bool:
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                print("Error: Non-existent edge")
            return True
        return False

    # Prints the Graph object
    def display_graph(self):
        if not self.adj_list:
            print("Empty graph")
        else:
            for vertex in self.adj_list:
                print(vertex, ":", self.adj_list[vertex])


if __name__ == "__main__":
    print("\n----- Test: Instantiates a Graph -----\n")
    my_graph = Graph()
    print("graph:")
    my_graph.display_graph()

    print("\n----- Test: Adds a vertex in a Graph -----\n")
    my_graph.add_vertex("A")
    print("graph:")
    my_graph.display_graph()

    print("\n----- Test: Adds an edge in a Graph -----\n")
    my_graph.add_vertex(1)
    my_graph.add_vertex(2)
    my_graph.add_edge(1, 2)
    print("graph:")
    my_graph.display_graph()

    print("\n----- Test: Removes an edge in a Graph -----\n")
    my_graph.remove_edge(1, 2)
    print("graph:")
    my_graph.display_graph()

    print("\n----- Test: Removes an edge in a Graph with multiple edges -----\n")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.add_edge("A", "B")
    my_graph.add_edge("A", "C")
    my_graph.add_edge("B", "C")
    print("graph:")
    my_graph.display_graph()
    print("")

    print("removed ('A', 'B') edge between vertex 'A' and vertex 'B'")
    my_graph.remove_edge("A", "B")
    print("graph:")
    my_graph.display_graph()

    print("\n----- Test: Tries to remove a non-existent edge in a Graph -----\n")
    my_graph.remove_edge("A", 1)
    print("graph:")
    my_graph.display_graph()

    print("\n----- Test: Removes a vertex in a Graph with multiple edges -----\n")
    my_graph.add_vertex("D")
    my_graph.add_edge("D", "A")
    my_graph.add_edge("D", "B")
    my_graph.add_edge("D", "C")
    print("graph:")
    my_graph.display_graph()
    print("")

    print("removed 'D' vertex along with its edges, ('D', 'A'), ('D', 'B'), ('D', 'C')")
    my_graph.remove_vertex("D")
    print("graph:")
    my_graph.display_graph()
