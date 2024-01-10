class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ar_hash = Counter(arr1)
        ar_container = []
        for i in arr2:
            ar_container.extend(i for _ in range(ar_hash[i]))
            ar_hash.pop(i)
        n_li = []
        for i in ar_hash:
            n_li.extend(i for _ in range(ar_hash[i]))
        n_li.sort()
        ar_container.extend(n_li)
        return ar_container
        