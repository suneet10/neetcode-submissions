class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def trav(start,arr,curr):

            if curr == target:
                res.append(list(arr))
                return

            elif curr > target:
                return

            for i in range(start,len(nums)):
                arr.append(nums[i])
                trav(i,arr,curr+nums[i])
                arr.pop()

        trav(0,[],0)
        return res