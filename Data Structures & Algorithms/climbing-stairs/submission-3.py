class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        i = 3
        x = 2
        y = 1

        while i <= n:

            tmp = x
            x = tmp + y
            y = tmp

            i += 1

        return x
            



