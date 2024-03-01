# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, val1, val2):
            if val1 > root.val and val2 > root.val:
                return dfs(root.right, val1, val2)
            elif val1 < root.val and val2 < root.val:
                return dfs(root.left, val1, val2)
            else:
                return root
        return dfs(root, p.val, q.val)