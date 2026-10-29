class Solution:

    arr = [0] * 2

    def climbStairs(self, n: int) -> int:

        arr = [0] * (n+1)
        
        def trav(n):
            print(n)
            if n <= 2:
                return n

            if arr[n-1] != 0:
                return arr[n-1] + arr[n-2]

            else:
                arr[n] = trav(n-1) + trav(n-2)
                return arr[n]
        ans = trav(n)
        print(arr)
        return ans
            



