class Solution:
    def isValid(self, s: str) -> bool:

        def reverse(x):

            if x == ")":
                return "("

            elif x == "}":
                return "{"

            elif x == "]":
                return "["

        arr = [1]
        
        for i in list(s):

            if arr[-1] == reverse(i):
                arr.pop()

            else:
                arr.append(i)

        if arr == [1]:
            return True
        else:
            return False