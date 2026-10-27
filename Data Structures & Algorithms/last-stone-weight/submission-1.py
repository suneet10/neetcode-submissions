class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = sorted(stones)

        while len(stones) > 1:

            x = stones.pop()
            y = stones.pop()

            if x != y:
                stones.append(abs(x-y))
                stones = sorted(stones)

        if stones:
            return stones[-1]
        return 0