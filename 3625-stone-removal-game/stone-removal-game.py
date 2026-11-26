class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = n
        remove = 10
        i = 1
        while stones >= remove:
            stones -= remove
            i += 1
            remove -= 1

        if i%2!=0:
            return False
        else:
            return True

          