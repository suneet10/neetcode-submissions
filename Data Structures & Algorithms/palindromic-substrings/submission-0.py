class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        
        def checkPal(left,right):

            nonlocal count

            if left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                checkPal(left-1,right+1)

        for i in range(len(s)):

            checkPal(i,i)

            if i+1 < len(s):
                checkPal(i,i+1)

        return count