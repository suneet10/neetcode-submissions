class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}
        
        for i in strs:

            if "".join(sorted(i)) in hashMap:

                hashMap["".join(sorted(i))].append(i)

            else:
                hashMap["".join(sorted(i))] = [i]

        return list(hashMap.values())