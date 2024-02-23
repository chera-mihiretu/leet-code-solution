class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = end = 0
        max_size = 0
        min_que = deque()
        max_que = deque()
        while end < len(nums):
            while min_que and min_que[-1] > nums[end]:
                min_que.pop()
            min_que.append(nums[end])

            while max_que and max_que[-1] < nums[end]:
                max_que.pop()
            max_que.append(nums[end])

            while max_que[0] - min_que[0] > limit:
                if nums[start] == max_que[0]:
                    max_que.popleft()
                if nums[start] == min_que[0]:
                    min_que.popleft()

                start += 1
                
            max_size = max(max_size, end-start +1)
            end += 1
        return max_size


            
