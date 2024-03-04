class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        answer = [float('inf')]
        def share(li, cur_li):
            if not li:
                val = max(cur_li)
                answer[0] = min(val, answer[0])
                return 
            for i in range(len(cur_li)):
                copy_list = cur_li.copy()
                copy_list[i] += li[0]
                if copy_list[i] > answer[0]:
                    continue
                share(li[1:], copy_list)
        cur_li = [0] * k
        share(cookies, cur_li)
        return answer[0]
