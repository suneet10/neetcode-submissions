class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1

        for i in dic:
            if dic[i] > len(nums)//2:
                return i
        