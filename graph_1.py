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
        if from_node in self.graph and to_node in self.graph:
            self.graph[from_node].append(to_node)
        elif from_node in self.graph:
            self.add_node(to_node)
            self.add_edge(from_node, to_node)
        else:
            self.add_node(from_node)
            self.add_edge(from_node, to_node)

    def del_node(self, node):
        del self.graph[node] 

    def del_edge(self, from_node, to_node):
        self.graph[from_node].remove(to_node)

    def nodes(self):
        node_res = []
        nodes = self.graph.keys()
        for item in nodes:
            node_res.append(item)
        return node_res
    
    def edges(self):
        edge_res = ''
        for node, edge in self.graph.items():
            if edge != []:
                for i in range(0, len(edge)):
                    edge_res += '(' + str(node) + '-' + str(edge[i]) + ')'
            else:
                return 'No Edges'
        return edge_res

    def has_node(self, node):
        return node in self.graph
    
    def neighbours(self, node):
        return self.graph[node]
    
    def adjacent(self, from_node, to_node):
        return to_node in self.graph[from_node]