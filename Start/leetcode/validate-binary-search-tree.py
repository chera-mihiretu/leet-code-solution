# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validity(root, bound):
            if not root:
                return True
            if bound[0] < root.val < bound[1]:
                return validity(root.left, (bound[0], root.val)) and validity(root.right, (root.val, bound[1]))
            else:
                return False
        return validity(root, (float('-inf'), float('inf')))

