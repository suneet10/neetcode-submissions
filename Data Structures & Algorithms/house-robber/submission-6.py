class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:

            return nums[0]

        x = max(nums[0],nums[1])
        y = nums[0]

        for i in range(2,len(nums)):

            temp = x
            x = max(x,y+nums[i])
            y = temp

        return x
