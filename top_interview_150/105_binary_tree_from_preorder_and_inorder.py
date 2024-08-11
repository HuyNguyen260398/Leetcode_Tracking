# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # The first element in preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the index of the root in inorder
        # This index divides the inorder array into left and right subtrees.
        mid = inorder.index(root_val)

        # Recursively build the left and right subtrees

        # The left subtree is built from the next mid elements in preorder and the first mid elements in inorder.
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # The right subtree is built from the remaining elements in preorder and the elements after mid in inorder.
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
