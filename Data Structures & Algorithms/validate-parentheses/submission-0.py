class Solution:
    def isValid(self, s: str) -> bool:

        def reverse(x):

            if x == ")":
                return "("

            elif x == "}":
                return "{"

            elif x == "]":
                return "["

        arr = []
        
        for i in list(s):

            if i == "(" or i == "{" or i == "[":

                arr.append(i)

            else:

                if arr[-1] != reverse(i):
                    return False

                else:
                    arr.pop()

        if arr == []:
            return True