class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):

                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1

        if obstacleGrid[-1][-1] == -1 or obstacleGrid[0][0] == -1:
            return 0

        prev = [0 for _ in range(len(obstacleGrid[0]))]

        for i in range(len(obstacleGrid)-1,-1,-1):

            if obstacleGrid[i][-1] != -1 and prev[-1] != -1:
                obstacleGrid[i][-1] = 1

            for j in range(len(obstacleGrid[0])-2,-1,-1):

                if obstacleGrid[i][j] == -1:
                    continue

                if prev[j] != -1:
                    y = prev[j]
                else:
                    y = 0

                if obstacleGrid[i][j+1] != -1:
                    x = obstacleGrid[i][j+1]
                else:
                    x = 0

                obstacleGrid[i][j] = x + y

            prev = obstacleGrid[i]

        # print(obstacleGrid)

        return obstacleGrid[0][0]