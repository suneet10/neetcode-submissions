class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        arr = [0] * len(nums)
        arr[0] = 1

        for i in range(1,len(nums)):
            
            m = 1

            for j in range(i-1,-1,-1):

                if nums[j] < nums[i]:

                    m = max(arr[j] + 1,m)

            arr[i] = m

        return max(arr)

