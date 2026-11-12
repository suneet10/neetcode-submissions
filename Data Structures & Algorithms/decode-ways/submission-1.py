class Solution:
    def numDecodings(self, s: str) -> int:

        # s = list(s)

        if s[0] == "0":
            return 0

        if len(s) < 2:
            return 1

        y = 1
        
        if s[1] == '0':
            if s[0] == '1' or s[0] == '2':
                x = 1
            else:
                return 0
        else:
            if int(s[0:2]) <= 26:
                x = 2
            else:
                x = 1

        for i in range(2,len(s)):

            temp = x
            if s[i] != '0' and int(s[i-1:i+1]) <= 26:
                if int(s[i-1:i+1]) < 10:
                    x = temp
                else:
                    x = y + temp
            elif s[i] != '0':
                x = temp
            else:
                if s[i-1] == '2' or s[i-1] == '1':
                    x = y
                else:
                    return 0
            y = temp
        
        return x