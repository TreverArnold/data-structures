class Graph:
    def __init__(self, iterable=None):
        self.graph = {}
        if iterable is not None:
            for item in iterable:
                self.add_node(item)

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, from_node, to_node):
        self.add_node(from_node)
        self.add_node(to_node)
        self.graph[from_node].append(to_node)
        self.graph[to_node].append(from_node)

    def del_node(self, node):
        if node in self.graph:
            for neighbor in self.graph[node]:
                self.graph[neighbor].remove(node)
            del self.graph[node]
        else:
            raise ValueError("Node is not in graph")

    def del_edge(self, from_node, to_node):
        if from_node in self.graph:
            self.graph[from_node].remove(to_node)
            self.graph[to_node].remove(from_node)
        else:
            raise ValueError("Edge is not in graph")

    def nodes(self):
        return list(self.graph.keys()) if list(self.graph.keys()) != [] else None

    def edges(self):
        edge_set = set()
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                edge_set.add(tuple(sorted((node, neighbor))))
        return list(edge_set) or 'No Edges'

    def has_node(self, node):
        return node in self.graph
    
    def neighbours(self, node):
        if node in self.graph:
            if self.graph[node] != []:
                return self.graph[node]
            return None
        else:
            raise ValueError("Node is not in graph")
    
    def adjacent(self, node1, node2):
        if node1 in self.graph:
            if node2 in self.graph: 
                if node2 in self.graph[node1] or node1 in self.graph[node2]:
                    return True
            return False
        else:
            raise ValueError("Node is not in graph")
