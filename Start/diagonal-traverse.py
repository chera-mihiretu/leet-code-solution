class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        _hash = {}
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row+col in _hash:
                    _hash[row+col].append(mat[row][col])
                else:
                    _hash[row+col] = [mat[row][col]]
        array = []
        for i, ar in _hash.items():
            if i % 2:
                for element in ar:
                    array.append(element)
            else:
                for element in ar[::-1]:
                    array.append(element)
        return array