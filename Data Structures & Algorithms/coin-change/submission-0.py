class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        arr = [0] * (amount+1)
        # arr[0] = float('inf')
        
        for i in range(1,len(arr)):

            fewest = float('inf')

            for j in coins:

                if j > i:
                    continue
                else:
                    x = i-j
                    x = 1 + arr[x]
                    fewest = min(fewest,x)
            arr[i] = fewest

        if arr[-1] == float('inf'):
            return -1
        return arr[-1]
