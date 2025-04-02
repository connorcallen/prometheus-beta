import pytest
from src.linked_list_reversal import Node, LinkedList

def test_node_creation():
    """Test basic node creation"""
    node = Node(5)
    assert node.value == 5
    assert node.next is None

def test_linked_list_append():
    """Test appending nodes to a linked list"""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]

def test_reverse_first_n_nodes_basic():
    """Test reversing the first n nodes"""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    
    ll.reverse_first_n_nodes(3)
    assert ll.to_list() == [3, 2, 1, 4, 5]

def test_reverse_first_n_nodes_full_list():
    """Test reversing the entire list"""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    ll.reverse_first_n_nodes(3)
    assert ll.to_list() == [3, 2, 1]

def test_reverse_first_n_nodes_single_element():
    """Test reversing a list with a single element"""
    ll = LinkedList()
    ll.append(1)
    
    ll.reverse_first_n_nodes(1)
    assert ll.to_list() == [1]

def test_reverse_first_n_nodes_empty_list():
    """Test reversing an empty list"""
    ll = LinkedList()
    
    ll.reverse_first_n_nodes(0)
    assert ll.to_list() == []

def test_reverse_first_n_nodes_negative_n():
    """Test that reversing with a negative n raises a ValueError"""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    
    with pytest.raises(ValueError, match="Number of nodes to reverse must be non-negative"):
        ll.reverse_first_n_nodes(-1)

def test_reverse_first_n_nodes_more_than_list_length():
    """Test reversing more nodes than exist in the list"""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    ll.reverse_first_n_nodes(5)
    assert ll.to_list() == [3, 2, 1]