class Solution:

    arr = [0] * 2

    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        arr = [0] * (n+1)
        arr[1] = 1
        arr[2] = 2
        
        def trav(n):

            if arr[n] == 0:
                arr[n] = trav(n-1) + trav(n-2)

            return arr[n]

        return trav(n)
            



