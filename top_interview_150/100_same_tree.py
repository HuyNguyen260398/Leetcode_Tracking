# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both node is null => identical
        if p is None and q is None:
            return True
        
        # if one of the node is null => not identical
        if p is None or q is None:
            return False

        # if the value is equal =>  the check child node (left, right) recursively
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # the value is not equal => return false
        return False