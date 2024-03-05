# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        answer = [0]
        def maxA(root):
            if not root.left and not root.right:
                return [root.val, root.val]
            left = right = [float('inf'), float('-inf')]
            if root.left:
                left = maxA(root.left)
            if root.right:
                right = maxA(root.right)
            
            answer[0] = max(answer[0], abs(root.val-min(left[0], right[0])), abs(root.val-max(left[1], right[1])))

            return [min(right[0], left[0], root.val), max(left[1], right[1], root.val)]

        maxA(root)
        return answer[0]