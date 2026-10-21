class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        res = []

        def trav(start,arr):
            if list(arr) not in res:
                res.append(list(arr))

            for i in range(start,len(nums)):
                arr.append(nums[i])
                trav(i+1,arr)
                arr.pop()

        trav(0,[])

        return res
