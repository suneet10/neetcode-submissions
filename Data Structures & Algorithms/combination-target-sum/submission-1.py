class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def trav(start,arr):

            if sum(arr) == target:
                res.append(list(arr))
                return

            elif sum(arr) > target:
                return

            for i in range(start,len(nums)):
                arr.append(nums[i])
                trav(i,arr)
                arr.pop()

        trav(0,[])
        return res