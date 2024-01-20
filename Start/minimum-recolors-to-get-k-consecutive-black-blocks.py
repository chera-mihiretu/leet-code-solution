class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_count = 0
        for i in range(k):
            if blocks[i] == "W":
                w_count +=1
        min_count = w_count
        start = 0
        end = k-1
        while end < len(blocks):
            if blocks[start] == "W":
                w_count -= 1
            start += 1
            end += 1
            if end < len(blocks) and blocks[end] == "W":
                w_count += 1
            if end < len(blocks):
                min_count = min(min_count, w_count)
        return min_count
                    