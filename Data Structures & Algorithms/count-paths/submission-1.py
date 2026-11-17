class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # cache = [[0] * n for _ in range(m)]
        cache = [[0 for _ in range(n)] for _ in range(m)]
        cache[m-1][n-1] = 1

        def trav(r,c):
            
            if r == m or c == n:
                return 0
            
            if cache[r][c] != 0:
                return cache[r][c]

            cache[r][c] = trav(r+1,c) + trav(r,c+1)
            return cache[r][c]

        return trav(0,0)
