class Solution:
    def rob(self, nums: List[int]) -> int:
        
        arr = [-1]*len(nums)

        arr[0] = nums[0]
        arr[1] = nums[1]

        for i in range(2,len(nums)):
            
            arr[i] = max(arr[:i-1]) + nums[i]

        return max(arr)