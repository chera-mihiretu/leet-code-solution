# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash_table = defaultdict(list)
        def dfs(root, depth):
            if not root:
                return
            hash_table[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        li = list(hash_table.values())
        for i in range(1, len(li), 2):
            li[i].reverse()
        return li

        