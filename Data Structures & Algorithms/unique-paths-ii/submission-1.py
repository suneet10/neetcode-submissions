class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):

                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1

        if obstacleGrid[-1][-1] == -1 or obstacleGrid[0][0] == -1:
            return 0

        obstacleGrid[-1][-1] = 1

        def trav(r,c):

            if r == len(obstacleGrid) or c == len(obstacleGrid[0]):
                return 0
            if obstacleGrid[r][c] != 0:
                if obstacleGrid[r][c] != -1:
                    return obstacleGrid[r][c]
                else:
                    return 0
            
            obstacleGrid[r][c] = trav(r+1,c) + trav(r,c+1)
            return obstacleGrid[r][c]

        return trav(0,0)