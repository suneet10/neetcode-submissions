class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        s = list(s)
        left = -1
        dic = {}
        ans = 0

        for i in range(len(s)):

            if s[i] not in dic:
                dic[s[i]] = 0
            dic[s[i]] += 1

            x = (sum(dic.values())-dic[max(dic, key=dic.get)])

            # print(s[i],dic,x,ans,sum(dic.values()))
            
            if x > k:
                print(1)
                left += 1
                dic[s[left]] -= 1

            # print(dic,x,ans,sum(dic.values()))
            
            ans = max(ans,sum(dic.values()))

        return ans



