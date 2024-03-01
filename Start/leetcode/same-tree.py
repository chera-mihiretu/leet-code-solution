# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        tree_one = deque([p])
        tree_two = deque([q])
        while tree_one and tree_two:
            node1 = tree_one.popleft()
            node2 = tree_two.popleft()
            if node1 and node2:
                if node1.val != node2.val:
                    return False
            elif node1 != node2:
                return False
            if node1:
                tree_one.append(node1.left)
                tree_one.append(node1.right)
            if node2:
                tree_two.append(node2.left)
                tree_two.append(node2.right)
        if len(tree_one) == len(tree_two):
            return True
        return False

        

        