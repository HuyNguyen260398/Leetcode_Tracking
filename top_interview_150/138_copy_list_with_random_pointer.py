# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # create a dictionary to store the mapping between the original nodes and new nodes
        node_map = {}

        # first pass: create new nodes without random pointers
        iter_node = head
        while iter_node:
            node_map[iter_node] = Node(iter_node.val)
            iter_node = iter_node.next

        # second pass: set next and random pointers for the new nodes
        iter_node = head
        while iter_node:
            new_node = node_map[iter_node]
            new_node.next = node_map.get(iter_node.next)
            new_node.random = node_map.get(iter_node.random)
            iter_node = iter_node.next

        # return the head of the copied linked list
        return node_map[head]