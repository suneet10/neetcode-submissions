class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        arr = [0] * len(nums)
        arr[0] = 1

        for i in range(1,len(nums)):

            for j in range(i-1,-1,-1):

                if nums[j] < nums[i]:

                    arr[i] = arr[j] + 1
                    break

            if arr[i] == 0:
                arr[i] = 1

        return max(arr)

