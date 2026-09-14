class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dic = {}

        for i in list(s):

            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for i in list(t):

            if i in dic:
                dic[i] -= 1
            else:
                return False

        for i in dic.values():
            if i != 0:
                return False

        return True