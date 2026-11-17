class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def trav(r,c):
            
            if r == m or c == n:
                return 0
            
            if r == m-1 and c == n-1:
                return 1

            return trav(r+1,c) + trav(r,c+1)

        return trav(0,0)