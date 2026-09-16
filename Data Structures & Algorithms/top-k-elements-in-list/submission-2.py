class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}

        for i in nums:

            if i in dic:
                dic[i] += 1

            else:
                dic[i] = 1

        arr = [0] * (len(nums)+1)

        for i in dic:

            if arr[dic[i]] == 0:
                arr[dic[i]] = [i]
            
            else:
                arr[dic[i]].append(i)

        ans = []

        for i in range(len(arr)-1,0,-1):

            if arr[i] != 0:
                ans += arr[i]

            if len(ans) >= k:
                return ans[0:k]