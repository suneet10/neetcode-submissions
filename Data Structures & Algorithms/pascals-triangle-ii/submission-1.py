class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    
        arr = [1]
        ans = [1]

        for i in range(rowIndex+2):

            ans = [0] * i

            for j in range(len(ans)):

                if j == 0 or j == len(ans)-1:
                    ans[j] = 1
                else:
                    ans[j] = arr[j-1] + arr[j]

            arr = ans

        return ans
