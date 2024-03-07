# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        tree_left = deque([root.left])
        tree_right = deque([root.right])
        while tree_left and tree_right:
            node_l = tree_left.popleft()
            node_r = tree_right.popleft()
            if node_l and node_r:
                if node_l.val != node_r.val:
                    return False
            else:
                if node_l != node_r:
                    return False
            if node_l:
                tree_left.append(node_l.left)
                tree_left.append(node_l.right)
            if node_r:
                tree_right.append(node_r.right)
                tree_right.append(node_r.left)
        if len(tree_right) == len(tree_left):
            return True
        return False