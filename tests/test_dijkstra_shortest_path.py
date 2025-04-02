import pytest
from src.dijkstra_shortest_path import dijkstra, reconstruct_path

def test_basic_dijkstra():
    # Simple graph with known shortest paths
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances == {
        'A': 0,
        'B': 3,  # A -> C -> B
        'C': 2,  # A -> C
        'D': 6   # A -> C -> B -> D
    }
    
    # Test path reconstruction
    assert reconstruct_path(previous, 'A', 'D') == ['A', 'C', 'B', 'D']

def test_disconnected_node():
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {}  # Disconnected node
    }
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances['C'] == float('inf')
    assert previous['C'] is None

def test_single_node_graph():
    graph = {
        'A': {}
    }
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances['A'] == 0
    assert previous['A'] is None

def test_error_handling():
    graph = {
        'A': {'B': 1},
        'B': {'A': 1}
    }
    
    # Test start node not in graph
    with pytest.raises(ValueError, match="Start node 'C' not found in graph"):
        dijkstra(graph, 'C')

def test_path_reconstruction():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    _, previous = dijkstra(graph, 'A')
    
    # Test valid path reconstruction
    assert reconstruct_path(previous, 'A', 'D') == ['A', 'C', 'B', 'D']
    
    # Test path to self
    assert reconstruct_path(previous, 'A', 'A') == ['A']

def test_path_reconstruction_errors():
    graph = {
        'A': {'B': 1},
        'B': {'A': 1}
    }
    
    _, previous = dijkstra(graph, 'A')
    
    # Test end node not in graph
    with pytest.raises(ValueError, match="End node 'C' not found in previous nodes"):
        reconstruct_path(previous, 'A', 'C')
    
    # Test no path exists
    graph_no_path = {
        'A': {},
        'B': {}
    }
    
    _, previous_no_path = dijkstra(graph_no_path, 'A')
    
    with pytest.raises(ValueError, match="No path exists from A to B"):
        reconstruct_path(previous_no_path, 'A', 'B')

def test_weighted_graph():
    graph = {
        'New York': {'Boston': 4, 'Philadelphia': 2},
        'Boston': {'Philadelphia': 6},
        'Philadelphia': {'Washington DC': 3},
        'Washington DC': {}
    }
    
    distances, previous = dijkstra(graph, 'New York')
    
    assert distances['Washington DC'] == 5  # New York -> Philadelphia -> Washington DC
    assert reconstruct_path(previous, 'New York', 'Washington DC') == ['New York', 'Philadelphia', 'Washington DC']