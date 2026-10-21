class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def trav(start,path):

            res.append(list(path))

            for i in range(start,len(nums)):
                path.append(nums[i])
                trav(i+1,path)
                path.pop()

        trav(0,[])
        return res