from typing import List, Dict, Set

def find_strongly_connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find strongly connected components in a directed graph using Kosaraju's Algorithm.
    
    Args:
        graph (Dict[int, List[int]]): A dictionary representing the directed graph,
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        List[List[int]]: A list of strongly connected components, where each component 
                         is a list of nodes that are mutually reachable.
    
    Raises:
        ValueError: If the input graph is empty or None.
    
    Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    Space Complexity: O(V)
    """
    # Validate input
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    def dfs_first_pass(node: int):
        """First DFS pass to record finishing times."""
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_first_pass(neighbor)
        stack.append(node)
    
    def dfs_second_pass(node: int, component: List[int]):
        """Second DFS pass to find strongly connected components."""
        visited.add(node)
        component.append(node)
        for neighbor in reversed_graph.get(node, []):
            if neighbor not in visited:
                dfs_second_pass(neighbor, component)
    
    # Ensure all graph nodes are included in the graph dictionary
    full_graph = {node: graph.get(node, []) for node in set(graph.keys()).union(*graph.values())}
    
    # First pass: DFS and fill stack with nodes
    visited = set()
    stack = []
    for node in full_graph:
        if node not in visited:
            dfs_first_pass(node)
    
    # Create reversed graph
    reversed_graph = {}
    for node, neighbors in full_graph.items():
        for neighbor in neighbors:
            if neighbor not in reversed_graph:
                reversed_graph[neighbor] = []
            if node not in reversed_graph:
                reversed_graph[node] = []
            reversed_graph[neighbor].append(node)
    
    # Second pass: Find strongly connected components
    visited.clear()
    strongly_connected_components = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs_second_pass(node, component)
            strongly_connected_components.append(component)
    
    return strongly_connected_components