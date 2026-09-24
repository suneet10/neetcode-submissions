class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        arr = list(text)
        arr2 = list("balloon")
        count = 0

        for i in arr:
            # print(i,arr2)

            if arr2 == []:
                count += 1
                arr2 = list("balloon")

            if i in arr2:
                arr2.remove(i)

        if arr2 == []:
            count += 1

        return count

