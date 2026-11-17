class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev = [0 for _ in range(n)]

        for i in range(m):
            
            curr = [0 for _ in range(n)]
            curr[-1] = 1
            
            for j in range(n-2,-1,-1):

                curr[j] = curr[j+1] + prev[j]

            prev = curr

        return curr[0]