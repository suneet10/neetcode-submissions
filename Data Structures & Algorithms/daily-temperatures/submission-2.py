class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [temperatures[0]]
        ans = [0]*len(temperatures)

        for i in range(1,len(temperatures)):
            count = 1
            s = 0
            while stack != [] and temperatures[i] > stack[-1]:
                # print(temperatures[i],i-count,stack,s)
                if ans[i-count] == 0:
                    s += 1
                    ans[i-count] = s
                    stack.pop()
                else:
                    # s += ans[i-count]
                    s += 1
                count += 1
                

            stack.append(temperatures[i])

        return ans
