class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        
        def trav(index,path):

            if index == len(nums):
                 result.append(path[:])
                 return

            path.append(nums[index])
            trav(index+1,path)
            path.pop()

            trav(index+1,path)

        trav(0,[])
        return result