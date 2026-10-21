class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def trav(curr,ans):
            # print(res,curr,ans)

            if curr == target:
                a = sorted(ans[:])
                if a not in res:
                    res.append(a)
                return

            elif curr > target:
                return

            for i in nums:

                curr += i
                ans.append(i)
                trav(curr,ans)
                curr -= i
                ans.pop()

                # trav(curr,ans)

        trav(0,[])
        return res