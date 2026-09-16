class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}

        for i in nums:

            if i in dic:
                dic[i] += 1

            else:
                dic[i] = 1

        dic = dict(sorted(dic.items(), key=lambda item: item[1],reverse=True))
        arr = list(dic.keys())

        return arr[0:k]