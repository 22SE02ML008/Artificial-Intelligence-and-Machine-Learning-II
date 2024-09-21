class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

class Edge:
    def __init__(self, relation, node):
        self.relation = relation
        self.node = node

cat = Node("Cat")
animal = Node("Animal")
tail = Node("Tail")

cat.add_edge(Edge("isA", animal))
cat.add_edge(Edge("has", tail))

def display_network(node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return
    visited.add(node)
    print(f"Node: {node.name}")
    for edge in node.edges:
        print(f"  {edge.relation} -> {edge.node.name}")
        display_network(edge.node, visited)

display_network(cat)
