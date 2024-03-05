class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.answer = 0 
        self.answer = max(self.addBST(root)[1], self.answer)
        return self.answer if self.answer > 0 else 0 

    def addBST(self, root):
        left = right = None
        if not root.right and not root.left:
            return ((root.val, root.val), root.val)
        if root.left:
            left = self.addBST(root.left)
        if root.right:
            right = self.addBST(root.right)
        self.answer = max(self.answer, max(left[1] if left else 0, right[1] if right else 0))
        
        if not left:
            if len(right[0]) != 1 and root.val < right[0][0]:
                return ((root.val, right[0][1]), right[1] + root.val)
            return ([False], right[1])
        if not right:
            if len(left[0]) != 1 and root.val > left[0][1]:
                return ((left[0][0], root.val), left[1] + root.val)
            return ([False], left[1])
        if len(left[0]) == 1 or len(right[0]) == 1:
            return ([False], max(left[1], right[1]))
        if left[0][1] < root.val < right[0][0]:
            return ((left[0][0], right[0][1]), root.val + left[1] + right[1])
        return ([False], max(left[1], right[1]))
            
                
