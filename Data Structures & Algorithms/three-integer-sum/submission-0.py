class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        left = 0
        right = len(nums)-1
        # print(nums)
        i = 1

        while i in range(1,len(nums)-1):

            if left < i and i < right:

                check = nums[left] + nums[i] + nums[right]
                # print([nums[left],nums[i],nums[right]],[left,i,right],check)
                
                if check == 0:
                    if [nums[left],nums[i],nums[right]] not in ans:
                        ans.append([nums[left],nums[i],nums[right]])
                    i += 1
                
                elif check < 0:
                    left += 1
                    i += 1

                else:
                    right -= 1

            else:
                break

        return ans
