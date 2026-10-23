class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        flag = [0] * len(nums)

        def trav(arr):
            
            if len(arr) == len(nums):
                res.append(list(arr))
                return

            for i in range(len(nums)):
                if flag[i] == 0:
                    arr.append(nums[i])
                    flag[i] = 1
                    trav(arr)
                    arr.pop()
                    flag[i] = 0

        trav([])

        return res
