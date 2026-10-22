class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        res = []

        def trav(start,arr):
            res.append(list(arr))

            for i in range(start,len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                arr.append(nums[i])
                trav(i+1,arr)
                arr.pop()

        trav(0,[])

        return res
