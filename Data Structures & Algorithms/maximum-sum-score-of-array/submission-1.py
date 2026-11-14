class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        
        arr1 = [0] * len(nums)

        arr2 = [0] * len(nums)

        for i in range(len(nums)):

            if i == 0:
                arr1[i] = nums[i]

            else:
                arr1[i] = arr1[i-1] + nums[i]

        for i in range(len(nums)-1,-1,-1):

            if i == len(nums)-1:
                arr2[i] = nums[i]

            else:
                arr2[i] = arr2[i+1] + nums[i]


        return max(max(arr1),max(arr2))