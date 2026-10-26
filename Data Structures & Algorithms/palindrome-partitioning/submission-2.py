class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def checkPal(arr2):
            for i in arr2:
                temp = list(i)
                # print(temp)
                if len(temp) == 1:
                    continue
                x = 0
                y = len(temp)-1
                while x < y:
                    # print(1)
                    if temp[x] != temp[y]:
                        # print("Fails",temp)
                        return False
                    x += 1
                    y -= 1
            return True
        
        res = []

        def trav(curr,s1,arr):
            # print(arr)
            if curr == len(s):
                if checkPal([s1]):
                    arr.append(s1)
                    res.append(list(arr))
                    arr.pop()
                return
            
            trav(curr+1,s1+s[curr],arr)
            if checkPal([s1]):
                arr.append(s1)
                trav(curr+1,s[curr],arr)
                arr.pop()
            else:
                return

        trav(1,s[0],[])

        # res2 = []

        # for i in res:
        #     if checkPal(i):
        #         res2.append(i)

        return res
