class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n

        for i, row in enumerate(mat):
            if i % 2 == 0:
                if row[k:] + row[:k] != row:
                    return False
            else:
                if row[-k:] + row[:-k] != row:
                    return False

        return True