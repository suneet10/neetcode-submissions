class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        s_min = 101
        s_max = -1

        for i in range(1,len(prices)):

            if prices[i-1] < s_min:
                s_min = prices[i-1]
                s_max = -1
            
            if prices[i] > s_max:
                s_max = prices[i]
        # print(s_max,s_min)
        if s_max - s_min > 0:
            return s_max - s_min

        else:
            return 0