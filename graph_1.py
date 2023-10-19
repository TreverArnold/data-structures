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
        return edge_res if edge_res != '' else 'No Edges'

    def has_node(self, node):
        return node in self.graph
    
    def neighbours(self, node):
        res = []
        if self.graph[node] == []:
            return None
        for item in self.graph.items():
            if self.adjacent(item[0], node):
                res += str(item[0])
        return res
    
    def adjacent(self, node1, node2):
        try:
            if node2 in self.graph[node1] or node1 in self.graph[node2]:
                return True
            return False
        except KeyError:
            return False