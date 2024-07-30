# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # using inorder traversal to get the values in ascending order
        def inorderTraversal(root):
            res = []
            if root:
                res = inorderTraversal(root.left)
                res.append(root.val)
                res = res + inorderTraversal(root.right)
            return res

        values = inorderTraversal(root)

        # find the minimum difference
        min_dif = float('inf')
        for i in range(1, len(values)):
            min_dif = min(min_dif, values[i] - values[i-1])

        return min_dif
