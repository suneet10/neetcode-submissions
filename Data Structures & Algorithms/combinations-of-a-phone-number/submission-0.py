class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        index = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        def trav(curr,arr):

            if len(arr) == len(digits):
                res.append(arr)
                return

            for i in index[int(digits[curr])]:
                trav(curr+1,arr+i)

        if len(digits) == 0:
            return []

        trav(0,"")

        return res
                

            