# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from pyparsing import Optional


class Solution:
    # Hash Table
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        while head:
            if head not in visited_nodes:
                visited_nodes.add(head)
                head = head.next
            else:
                return True
        
        return False
    
    # Two Pointers
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    return True
        
        return False