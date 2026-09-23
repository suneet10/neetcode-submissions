class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        hashmap = {}
        
        for i in emails:
            s = ""
            flag = False
            arr = list(i)
            for j in range(len(arr)):

                if flag == "@":
                    s += arr[j]

                elif flag == "+" and arr[j] != "@":
                    continue

                elif arr[j] == "@":
                    flag = "@"
                    s += arr[j]

                elif flag != "@" and arr[j] == "+":
                    flag = "+"

                elif flag == False and arr[j] == ".":
                    continue
                
                else:
                    s += arr[j]

            hashmap[s] = 1

        return len(hashmap)

                