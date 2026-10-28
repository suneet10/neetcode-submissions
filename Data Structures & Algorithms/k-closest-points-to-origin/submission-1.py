class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def push(arr,val):
            
            arr.append(val)

            i = len(arr) - 1

            parent = arr[i//2]

            while i > 1 and ((parent[0]**2) + (parent[1]**2))**0.5 < ((arr[i][0]**2) + (arr[i][1]**2))**0.5:
                    
                temp = arr[i//2]
                arr[i//2] = arr[i]
                arr[i] = temp

                i = i//2

            return arr


        def pop(arr):
            print(arr)
            if len(arr) <=2:
                arr.pop()
                return arr
            arr[1] = arr.pop()

            i = 1

            while (2*i) < len(arr):
                
                if (2*i) + 1 < len(arr) and ((arr[(2*i) + 1][0])**2 + (arr[(2*i) + 1][1])**2)**0.5 > ((arr[i][0])**2 + (arr[i][1])**2)**0.5 and ((arr[(2*i) + 1][0])**2 + (arr[(2*i) + 1][1])**2)**0.5 > ((arr[(2*i)][0])**2 + (arr[(2*i)][1])**2)**0.5:

                    temp = arr[(2*i)+1]
                    arr[(2*i)+1] = arr[i]
                    arr[i] = temp

                    i = (2**i) + 1

                elif ((arr[2*i][0])**2 + (arr[2*i][1])**2)**0.5 > ((arr[i][0])**2 + (arr[i][1])**2)**0.5:

                    temp = arr[2*i]
                    arr[2*i] = arr[i]
                    arr[i] = temp

                    i = 2**i

                else:
                    break

            return arr




        heap = [[0,0]]

        heap.append(points[0])

        for i in range(1,len(points)):

            if len(heap)-1 < k:
                heap = push(heap,points[i])
            
            else:
                
                if ((heap[1][0]**2) + (heap[1][1]**2))**0.5 > ((points[i][0]**2)+(points[i][1]**2))**0.5:
                    heap = pop(heap)
                    heap = push(heap,points[i])
        print(heap)
        return heap[1:k+1]
