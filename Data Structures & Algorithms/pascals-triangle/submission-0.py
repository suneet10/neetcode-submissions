class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = [[1]]

        for i in range(1,numRows):

            arr = [0] * (i+1)

            for j in range(len(arr)):
                if j == 0 or j == len(arr)-1:
                    arr[j] = 1
                else:
                    arr[j] = ans[-1][j-1] + ans[-1][j]

            ans.append(arr)

        return ans