class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 1 - len(s1)
        s = list(s2)
        og_dic = {}
        for i in list(s1):
            if i not in og_dic:
                og_dic[i] = 0
            og_dic[i] += 1

        dic = {}
        for i in range(len(s)):

            if left > 0:
                if dic[s[left-1]] == 1:
                    dic.pop(s[left-1])
                else:
                    dic[s[left-1]] -= 1

            if s[i] not in dic:
                dic[s[i]] = 0
            dic[s[i]] += 1

            if dic == og_dic:
                return True
            # print(dic,og_dic)
            left += 1
        
        return False




                  