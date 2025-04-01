import pytest
from src.kosaraju_scc import find_strongly_connected_components

def test_basic_strongly_connected_components():
    # Simple graph with two strongly connected components
    graph = {
        0: [1],
        1: [2],
        2: [0],
        3: [4],
        4: [5],
        5: [3]
    }
    
    scc = find_strongly_connected_components(graph)
    
    # Check that there are two strongly connected components
    assert len(scc) == 2
    
    # Check that the components are correct
    assert sorted(scc[0]) == [0, 1, 2] or sorted(scc[1]) == [0, 1, 2]
    assert sorted(scc[0]) == [3, 4, 5] or sorted(scc[1]) == [3, 4, 5]

def test_single_node_components():
    # Graph with single-node components
    graph = {
        0: [],
        1: [],
        2: []
    }
    
    scc = find_strongly_connected_components(graph)
    
    # Each node should be its own component
    assert len(scc) == 3
    assert len(scc[0]) == 1
    assert len(scc[1]) == 1
    assert len(scc[2]) == 1

def test_fully_connected_graph():
    # Fully connected graph
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    
    scc = find_strongly_connected_components(graph)
    
    # Should be a single strongly connected component
    assert len(scc) == 1
    assert sorted(scc[0]) == [0, 1, 2]

def test_empty_graph_raises_error():
    # Empty graph should raise ValueError
    with pytest.raises(ValueError):
        find_strongly_connected_components({})

def test_complex_graph():
    # More complex graph with multiple components
    graph = {
        0: [1],
        1: [2, 3],
        2: [0],
        3: [4],
        4: [5],
        5: [3, 6],
        6: []
    }
    
    scc = find_strongly_connected_components(graph)
    
    # Verify the components
    assert len(scc) == 3
    
    # Components should be: 
    # [0, 1, 2], [3, 4, 5], [6]
    component_lengths = [len(comp) for comp in scc]
    assert sorted(component_lengths) == [1, 2, 3]

def test_graph_with_unreachable_nodes():
    # Graph with some unreachable nodes
    graph = {
        0: [1],
        1: [2],
        2: [0],
        3: [],
        4: [5],
        5: [4]
    }
    
    scc = find_strongly_connected_components(graph)
    
    # Should have three components
    assert len(scc) == 3
    
    # Verify the components
    component_sets = [set(comp) for comp in scc]
    assert any(component_sets[i] == {0, 1, 2} for i in range(len(component_sets)))
    assert any(component_sets[i] == {4, 5} for i in range(len(component_sets)))
    assert any(component_sets[i] == {3} for i in range(len(component_sets)))