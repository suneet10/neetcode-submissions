class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        x = nums[1]
        y = nums[0]
        
        

        for i in range(2,len(nums)):
            
            temp = x
            x = max(nums[i]+y,temp)
            y = temp

        return max(x,y)