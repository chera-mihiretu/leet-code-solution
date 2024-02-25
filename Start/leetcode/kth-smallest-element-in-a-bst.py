# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int, val = []) -> int:
        stack = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            stack.append(root.val)
            if root.right:
                traverse(root.right)
        traverse(root)
        return stack[k-1]
