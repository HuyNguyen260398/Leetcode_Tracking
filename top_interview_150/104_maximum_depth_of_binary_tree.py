# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            else:
                left_subtree = root.left
                current_left_depth = depth + 1
                left_depth = dfs(left_subtree, current_left_depth)

                right_subtree = root.right
                current_right_depth = depth + 1
                right_depth = dfs(right_subtree, current_right_depth)

                max_depth = max(left_depth, right_depth)
                return max_depth

        return dfs(root, 0)
    
    def maxDepth_shorten(self, root: TreeNode) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)