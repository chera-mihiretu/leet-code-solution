# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash = defaultdict(lambda:defaultdict(list))
        def dfs(root, pos):
            if not root:
                return
            dfs(root.left, (pos[0]+1, pos[1]-1))
            dfs(root.right, (pos[0]+1, pos[1]+1))
            hash[pos[1]][pos[0]].append(root.val)
        dfs(root, (0,0))

        li = list(hash.keys())
        li.sort()
        answer = []
        for i in range(len(li)):
            line = []
            an_l = list(hash[li[i]].keys())
            an_l.sort()
            for j in an_l:
                value = hash[li[i]][j]
                value.sort()
                line.extend(value)
            answer.append(line)
        return answer
