class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        # print(arr)
        return len(arr[-1])