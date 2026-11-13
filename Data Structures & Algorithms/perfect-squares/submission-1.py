class Solution:
    def numSquares(self, n: int) -> int:
        
        arr = [0] * (n+1)

        for i in range(1,len(arr)):

            fewest = float('inf')

            for j in range(1,101):

                if j*j > i:
                    break
                
                x = i - (j*j)
                x = 1 + arr[x]
                fewest = min(fewest,x)

            arr[i] = fewest

        # print(arr)
        return arr[-1]
