class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        arr = list(text)
        hashmap = {'b':0,'a':0,'l':0,'o':0,'n':0,}

        for i in arr:
            # print(i,arr2)

            if i in hashmap:
                hashmap[i] += 1

        hashmap['l'] = hashmap['l'] // 2
        hashmap['o'] = hashmap['o'] // 2

        print(hashmap)

        return min(hashmap.values())

