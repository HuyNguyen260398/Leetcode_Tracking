# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create the dummy node that always point to the head, becuase we need to return the head of the linked list
        dummy = ListNode()
        cur = dummy

        # loop through linked list
        while list1 and list2:

            if list1.val < list2.val:
                # append the value to the merged list
                cur.next = list1
                # then move to the next node
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        # after the loop, append the remaining node to the end of the merged list
        if list1:
            cur.next = list1
        else:
            cur.next = list2

        # return the next node after the dummny node (which is the head of the mearged list)
        return dummy.next

# https://youtu.be/eaRfv5VY7sI?si=xMFR32N6JHBG1Y5_
