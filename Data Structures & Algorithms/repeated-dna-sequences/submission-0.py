class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        dic = {}
        
        for i in range(len(s)):

            if s[i:i+10] not in dic:
                dic[s[i:i+10]] = 0
            dic[s[i:i+10]] += 1
        
        ans = []

        for i in dic:

            if len(i) == 10 and dic[i] > 1:
                ans.append(i)

        return ans
