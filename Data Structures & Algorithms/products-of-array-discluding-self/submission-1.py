class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        mult = 1
        zero = False
        count = 0
        # if sum

        for i in nums:

            if i != 0:
                mult *= i

            else: 
                zero = True
                count += 1

        ans = [0] * len(nums)

        if count >= len(nums)-1:
            return ans

        if zero == True:

            for i in range(len(nums)):

                if nums[i] == 0:
                    ans[i] = mult

        else:

            for i in range(len(nums)):

                ans[i] = mult//nums[i]

        return ans