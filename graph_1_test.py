from graph_1 import Graph

def test_innit():
    graph = Graph([1, 2, 3])
    graph.add_edge(1, 2)
    assert graph.edges() == 1