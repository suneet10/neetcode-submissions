class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def trav(o,c,arr):

            if len(arr) == n*2:
                res.append(arr)
                return

            if o < n:
                trav(o+1,c,arr+"(")

            if c < o:
                trav(o,c+1,arr+")")

        trav(0,0,"")

        return res
