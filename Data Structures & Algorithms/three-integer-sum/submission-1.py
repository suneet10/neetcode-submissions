class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        # print(nums)

        for i in range(0,len(nums)-2):

            left = i + 1
            right = len(nums)-1

            while left < right:

                check = nums[i] + nums[left] + nums[right]
                # print([nums[i],nums[left],nums[right]],[i,left,right],check)

                if check == 0:
                    if [nums[i],nums[left],nums[right]] not in ans:
                        ans.append([nums[i],nums[left],nums[right]])
                        left += 1
                    else:
                        # print(1)
                        break

                else:
                    if check < 0:
                        left += 1
                    else:
                        right -= 1
            

        return ans
