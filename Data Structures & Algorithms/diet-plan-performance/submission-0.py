class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        ans = 0

        if sum(calories[:k]) > upper:
            ans += 1
        elif sum(calories[:k]) < lower:
            ans -= 1
        t = sum(calories[:k])

        i = 1
        j = k

        while j<len(calories):

            t -= calories[i-1]
            t += calories[j]

            if t > upper:
                ans += 1
            elif t < lower:
                ans -= 1

            i += 1
            j += 1

        return ans


        
