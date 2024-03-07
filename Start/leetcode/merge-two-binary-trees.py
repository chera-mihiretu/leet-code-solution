# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            if root1 and root2:
                root1.val += root2.val
            if root1.right and root2.right:
                dfs(root1.right, root2.right)
            elif root1.right or root2.right:
                if not root1.right:
                    root1.right = TreeNode(0)
                elif not root2.right:
                    root2.right = TreeNode(0)
                dfs(root1.right, root2.right)
            if root1.left and root2.left:
                dfs(root1.left, root2.left)
            elif root1.left or root2.left:
                if not root1.left:
                    root1.left = TreeNode(0)
                elif not root2.left:
                    root2.left = TreeNode(0)
                dfs(root1.left, root2.left)
        node1 = TreeNode(0, root1)
        node2 = TreeNode(0, root2)
        dfs(node1, node2)
        return node1.left

