class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []

        for i in queries:
            
            if i[0] % len(nums) == 0:

                if (i[0] / len(nums)) % 2 == 0:
                    ans.append(nums[i[1]])
                else:
                    ans.append(-1)

            else:
                 
                x = i[0] % (2*len(nums))

                if x < len(nums):
                    arr = nums[x:]
                else:
                    x = x % len(nums)
                    arr = nums[:x]

                if i[1] < len(arr):
                    ans.append(arr[i[1]])
                else:
                    ans.append(-1)

        return ans

