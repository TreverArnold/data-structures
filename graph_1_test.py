from graph_1 import Graph

def test_innit():
    graph = Graph([1, 2, 3])
    assert graph.edges() == 'No Edges'
    assert graph.nodes() == [1, 2, 3]