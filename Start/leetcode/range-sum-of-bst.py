# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def treeTra(root):
            value = 0
            if root.left:
                value += treeTra(root.left)
            if low <= root.val <= high:
                value += root.val
            if root.right:
                value += treeTra(root.right)
            return value
        return treeTra(root)

