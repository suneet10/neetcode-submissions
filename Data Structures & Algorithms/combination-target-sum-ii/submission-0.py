class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)
        
        res = []

        def trav(start,arr):

            if sum(arr) == target:
                res.append(list(arr))
                return

            if sum(arr) < target:
                for i in range(start,len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    arr.append(candidates[i])
                    trav(i+1,arr)
                    arr.pop()
            
        trav(0,[])

        return res