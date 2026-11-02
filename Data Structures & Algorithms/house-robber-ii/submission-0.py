class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums[0],nums[1])

        x = max(nums[1],nums[0])
        y = nums[0]
         

        for i in range(2,len(nums)-1):
            
            temp = x
            x = max(nums[i]+y,temp)
            y = temp

        ans1 = max(x,y)

        x = max(nums[2],nums[1])
        y = nums[1]
         

        for i in range(3,len(nums)):
            
            temp = x
            x = max(nums[i]+y,temp)
            y = temp

        ans2 = max(x,y)

        return max(ans1,ans2)