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
                curr += nums[i]
                trav(i,arr,curr)
                arr.pop()
                curr -= nums[i]

        trav(0,[],0)
        return res