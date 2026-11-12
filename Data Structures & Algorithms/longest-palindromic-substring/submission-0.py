class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def checkPal(left,right):

            if left >= 0 and right < len(s) and s[left] == s[right]:
                return checkPal(left-1,right+1)
            else:
                return left,right

        longest = 0
        ll = 0

        for i in range(len(s)):

            l,r = checkPal(i,i)
            # print(i,l,r)
            x = (r-1)-(l+1)
            long_left = l+1

            if i+1 != len(s):
                l,r = checkPal(i,i+1)
                if (r-1)-(l+1) > x:
                    x = (r-1)-(l+1)
                    long_left = l+1

            if x > longest:
                longest = x
                ll = long_left
        # print(ll,longest)
        return s[ll:ll+longest+1]