class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # arr = [0] * len(cost)
        x,y = cost[0],cost[1]

        if len(cost) == 2:
            return min(cost)

        for i in range(2,len(cost)):

            temp = min(y+cost[i],x+cost[i])
            x = y
            y = temp

        return min(x,y)