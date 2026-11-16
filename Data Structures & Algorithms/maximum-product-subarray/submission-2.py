class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        larr = [0] * len(nums)
        sarr = [0] * len(nums)
        larr[0],sarr[0] = nums[0],nums[0]

        for i in range(1,len(nums)):
            larr[i] = max(larr[i-1]*nums[i],nums[i],sarr[i-1]*nums[i])
            sarr[i] = min(larr[i-1]*nums[i],nums[i],sarr[i-1]*nums[i])


        return max(larr)


