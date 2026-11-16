class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        arr = [False] * (len(s)+1)
        arr[0] = True

        for i in range(len(arr)):

            if arr[i]:
                # print(1,i)
                for j in wordDict:
                    # print(2,i,j)
                    # print(s[i:i+len(j)])
                    if s[i:i+len(j)] == j:
                        # print(3,i,j)
                        arr[i+len(j)] = True

        return arr[-1]