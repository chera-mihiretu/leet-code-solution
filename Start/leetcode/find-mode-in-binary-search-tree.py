# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hasher = defaultdict(int)
        max_oc = 0
        def mode(root):
            nonlocal max_oc
            if not root:
                return
            hasher[root.val] += 1
            max_oc = max(max_oc, hasher[root.val])
            if root:
                left = mode(root.left)
            if root:
                right = mode(root.right)
        answer = []
        mode(root)
        for val, oc in  hasher.items():
            if oc == max_oc:
                answer.append(val)    
        
        return answer