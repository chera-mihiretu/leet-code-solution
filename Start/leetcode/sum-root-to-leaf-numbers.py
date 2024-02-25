# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def summit(root,path=0):
            path = path * 10
            path +=  root.val
            if root.right or root.left:
                if root.right and root.left:
                    return summit(root.left, path) + summit(root.right, path)
                if root.left:
                    return summit(root.left, path)
                if root.right:
                    return summit(root.right, path)
            else:
                return path
        return summit(root)

        
        