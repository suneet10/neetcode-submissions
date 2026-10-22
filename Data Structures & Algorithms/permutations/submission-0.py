class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def trav(curr,arr):
            
            if len(arr) == len(nums):
                res.append(list(arr))
                return

            for i in range(len(nums)):
                if nums[i] not in arr:
                    arr.append(nums[i])
                    trav(curr,arr)
                    arr.pop()

        trav(0,[])

        return res
