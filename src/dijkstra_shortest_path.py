import heapq
from typing import Dict, List, Tuple, Optional

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Tuple[Dict[str, int], Dict[str, Optional[str]]]:
    """
    Implement Dijkstra's algorithm to find the shortest paths from a start node.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph.
                                           Keys are nodes, values are dictionaries of neighboring nodes and edge weights.
        start (str): Starting node for the shortest path calculation.
    
    Returns:
        Tuple containing:
        - Dict of shortest distances from start node to each node
        - Dict of previous nodes in the shortest path for each node
    
    Raises:
        ValueError: If the start node is not in the graph
    """
    # Validate input
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in graph")
    
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    # Priority queue to store nodes to visit
    pq = [(0, start)]
    
    # Track visited nodes to prevent redundant processing
    visited = set()
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if node already processed
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # Check neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Update if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous_nodes

def reconstruct_path(previous_nodes: Dict[str, Optional[str]], start: str, end: str) -> List[str]:
    """
    Reconstruct the shortest path between start and end nodes.
    
    Args:
        previous_nodes (Dict[str, Optional[str]]): Dictionary of previous nodes in shortest paths
        start (str): Starting node
        end (str): Destination node
    
    Returns:
        List[str]: Shortest path from start to end
    
    Raises:
        ValueError: If no path exists between start and end
    """
    path = []
    current = end
    
    # Validate input
    if end not in previous_nodes:
        raise ValueError(f"End node '{end}' not found in previous nodes")
    
    # Reconstruct path
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
        
        # Prevent infinite loop and detect unreachable destination
        if current == start:
            path.append(start)
            break
    
    # Check if path was successfully constructed
    if path[-1] != start:
        raise ValueError(f"No path exists from {start} to {end}")
    
    return list(reversed(path))