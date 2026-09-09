class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}
        
        for i in strs:

            count = [0] * 26

            for j in list(i):
                count[ord(j)-ord("a")] += 1

            count = tuple(count)

            if count in hashMap:
                hashMap[count].append(i)
            else:
                hashMap[count] = [i]

        return list(hashMap.values())