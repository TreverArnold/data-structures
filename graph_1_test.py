from graph_1 import Graph

def test_innit():
    graph = Graph([1, 2, 3])
    assert graph.edges() == 'No Edges'
    assert graph.nodes() == [1, 2, 3]

def test_add_node():
    graph = Graph([1, 2, 3])
    graph.add_node(4)
    assert graph.nodes() == [1, 2, 3, 4]
    assert graph.edges() == 'No Edges'

def test_del_node():
    graph = Graph([1, 2, 3, 4])
    graph.del_node(4)
    assert graph.nodes() == [1, 2, 3]
    assert graph.edges() == 'No Edges'

def test_add_edge():
    graph = Graph([1, 2, 3])
    graph.add_edge(1, 2)
    assert graph.edges() == '(1-2)'

def test_del_edge():
    graph = Graph([1, 2, 3])
    graph.add_edge(1, 2)
    graph.del_edge(1, 2)
    assert graph.edges() == 'No Edges'

def test_adjacent():
    graph = Graph([1, 2, 3])
    graph.add_edge(1, 2)
    assert graph.adjacent(1, 2) == True
    graph.del_edge(1, 2)
    assert graph.adjacent(1, 2) == False

def test_neighbors():
    graph = Graph([1, 2, 3])
    graph.add_edge(1, 2)
    assert graph.neighbours(1) == ['2']
    graph.del_edge(1, 2)
    assert graph.neighbours(1) == None

def test_comprehensive():
    graph = Graph()
    graph.add_node(1)
    assert graph.edges() == 'No Edges'
    assert graph.nodes() == [1]
    assert graph.neighbours(1) == None
    assert graph.adjacent(1, 2) == False
    graph.add_node(2)
    assert graph.edges() == 'No Edges'
    assert graph.nodes() == [1, 2]
    assert graph.neighbours(1) == None
    assert graph.adjacent(1, 2) == False
    graph.add_edge(1, 2)
    assert graph.edges() == '(1-2)'
    assert graph.nodes() == [1, 2]
    assert graph.neighbours(1) == ['2']
    assert graph.adjacent(1, 2) == True
    assert graph.adjacent(2, 1) == True
    graph.add_node(3)
    graph.add_edge(1, 3)
    assert graph.edges() == '(1-2)(1-3)'
    assert graph.nodes() == [1, 2, 3] 
    assert graph.neighbours(1) == ['2', '3']
    assert graph.adjacent(1, 2) == True
    assert graph.adjacent(1, 3) == True
    assert graph.adjacent(3, 1) == True
    graph.add_edge(2, 3)
    assert graph.edges() == '(1-2)(1-3)(2-3)'
    assert graph.nodes() == [1, 2, 3] 
    assert graph.neighbours(1) == ['2', '3']
    assert graph.neighbours(2) == ['1', '3']
    assert graph.neighbours(3) == ['1', '2']
    assert graph.adjacent(1, 2) == True
    assert graph.adjacent(1, 3) == True
    assert graph.adjacent(2, 3) == True
