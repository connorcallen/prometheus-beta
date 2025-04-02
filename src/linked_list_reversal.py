class Node:
    """
    Represents a node in a singly linked list.
    
    Attributes:
        value: The value stored in the node
        next: Reference to the next node in the list
    """
    def __init__(self, value=None):
        """
        Initialize a node with an optional value.
        
        Args:
            value: The value to be stored in the node (default None)
        """
        self.value = value
        self.next = None

class LinkedList:
    """
    A singly linked list implementation with methods for creation, 
    appending, and reversing.
    """
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
    
    def append(self, value):
        """
        Append a new node with the given value to the end of the list.
        
        Args:
            value: The value to be added to the list
        """
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def to_list(self):
        """
        Convert the linked list to a Python list for easy comparison.
        
        Returns:
            A list containing the values of the linked list nodes
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    def reverse_first_n_nodes(self, n):
        """
        Reverse the first n nodes of the linked list.
        
        Args:
            n (int): Number of nodes to reverse from the start of the list
        
        Raises:
            ValueError: If n is negative
        """
        # Handle invalid or edge cases
        if n < 0:
            raise ValueError("Number of nodes to reverse must be non-negative")
        
        if not self.head or n <= 1:
            return
        
        # Track the first n nodes
        prev = None
        current = self.head
        count = 0
        
        # Reverse first n nodes
        while current and count < n:
            # Store the next node before changing links
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move pointers forward
            prev = current
            current = next_node
            count += 1
        
        # Reconnect the reversed part with the rest of the list
        # If the head was the first node to be reversed
        self.head.next = current
        self.head = prev