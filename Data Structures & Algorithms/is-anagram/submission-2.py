class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ls = list(s)
        lt = list(t)

        dic = {}

        for i in ls:
            
            if i in dic:
                dic[i] += 1
            
            else:
                dic[i] = 1

        for j in lt:

            if j in dic:
                dic[j] -= 1

            else:
                return False

        
        for i in dic.values():
            if i!= 0:
                return False

        else:
            return True