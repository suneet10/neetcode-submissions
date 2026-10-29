class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        arr2 = [0] * len(arr)
        arr2[0] = 1
        arr2[1] = 1

        for i in range(2,len(arr)):
            if arr[i] == arr[i-1] + arr[i-2]:
                arr2[i] = 1
        
        ans = 0
        streak = 0
        for i in arr2:

            if i == 1:
                streak += 1
                ans = max(streak,ans)
            else:
                streak = 0

        if ans < 3:
            return 0
        return ans

