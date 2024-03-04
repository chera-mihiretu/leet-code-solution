# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBST(li):
            n = len(li)
            print(li)
            if n == 1:                                                  
                return TreeNode(li[0])                                    
            if n == 2:
                return TreeNode(li[1], TreeNode(li[0]))
            if n == 3:
                return TreeNode(li[1], TreeNode(li[0]), TreeNode(li[2]))
            
            if n % 2:
                right = makeBST(li[-(n//2):])
            else:
                right = makeBST(li[-(n//2-1):])
            left = makeBST(li[:n//2])

            return TreeNode(li[n//2], left, right)
        return makeBST(nums)
                
        
       
