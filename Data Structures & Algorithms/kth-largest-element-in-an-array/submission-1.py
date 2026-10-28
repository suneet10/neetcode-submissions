class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def push(arr,val):

            if len(arr) == 1:
                arr.append(val)
                return arr
            
            arr.append(val)
            i = len(arr)-1

            while i > 1 and arr[i] < arr[i//2]:

                temp = arr[i]
                arr[i] = arr[i//2]
                arr[i//2] = temp

                i = i//2

            return arr

        def pop(arr):

            if len(arr) == 2:
                arr.pop()
                return arr

            arr[1] = arr.pop()
            i = 1

            while 2*i < len(arr):

                if (2*i)+1 < len(arr) and arr[i] > arr[(2*i)+1] and arr[2*i] > arr[(2*i)+1]:

                    temp = arr[(2*i)+1]
                    arr[(2*i)+1] = arr[i]
                    arr[i] = temp

                    i = (2*i)+1

                elif arr[i] > arr[2*i]:

                    temp = arr[(2*i)]
                    arr[(2*i)] = arr[i]
                    arr[i] = temp

                    i = (2*i)

                else:
                    break

            return arr


        heap = [0]
    
        for i in nums:

            if len(heap) - 1 < k:
                heap = push(heap,i)

            else:

                if heap[1] < i:
                    heap = pop(heap)
                    heap = push(heap,i)

        return heap[1]


