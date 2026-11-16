class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        arr = [0] * len(nums)
        arr[0] = nums[0]

        for i in range(1,len(nums)):
            if nums[i] != 0 and nums[i-1] != 0:
                arr[i] = arr[i-1] * nums[i]
            elif nums[i-1] == 0:
                arr[i] = nums[i]
            else:
                arr[i] = 0


        return max(arr)


