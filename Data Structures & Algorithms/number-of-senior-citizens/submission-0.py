class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0

        for i in details:

            arr = list(i)

            age = (int(arr[-4])*10) + int(arr[-3])

            if age > 60:
                count += 1

        return count