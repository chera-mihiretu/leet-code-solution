class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def generate(left, right, li):
            if len(li) == (n * 2):
                answer.append(''.join(li))
                return
            if left < n:
                li.append('(')
                generate(left + 1 , right, li)
                li.pop()
            if right < left:
                li.append(')')
                generate(left , right + 1, li)
                li.pop()
        generate(0,0,[])
        return answer
