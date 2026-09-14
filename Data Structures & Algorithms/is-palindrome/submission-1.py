class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        arr = list(s.replace(" ","").lower())

        arr2 = []
        print(arr2)

        for i in arr:

            if ord(i) >= ord("a") and ord(i) <= ord("z"):
                arr2.append(i)
            
            elif ord(i) >= ord("0") and ord(i) <= ord("9"):
                arr2.append(i)

        arr = arr2

        i = 0
        j = len(arr)-1

        while i < j:

            if arr[i] != arr[j]:
                return False

            i += 1
            j -= 1

        return True