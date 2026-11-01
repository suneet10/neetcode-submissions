class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        nums.sort()
        prev = nums[0]
        for i in range(1,len(nums)):

            if prev != nums[i] - 1:
                return False
            prev = nums[i]

        return True