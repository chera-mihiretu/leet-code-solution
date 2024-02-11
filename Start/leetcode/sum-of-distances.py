class Solution:
  def distance(self, nums: List[int]) -> List[int]:
    ans = [0] * len(nums)
    index = collections.defaultdict(list)

    for i in range(len(nums)):
      index[nums[i]].append(i)

    for indices in index.values():
      n = len(indices)
      if n == 1:
        continue
      sumSoFar = sum(indices)
      prevIndex = 0
      for i in range(n):
        sumSoFar += (i - 1) * (indices[i] - prevIndex)
        sumSoFar -= (n - i - 1) * (indices[i] - prevIndex)
        ans[indices[i]] = sumSoFar
        prevIndex = indices[i]

    return ans