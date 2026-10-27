class Solution:
    def push(self,arr,val):

        arr.append(val)

        i = len(arr)-1

        while i > 1 and arr[i] > arr[i//2]:
            temp = arr[i]
            arr[i] = arr[i//2]
            arr[i//2] = temp

            i = i//2

        return arr

    def pop(self,arr):

        if len(arr) <= 2:
            return [arr[0]]

        arr[1] = arr.pop()
        i = 1
        while (2*i) < len(arr):

            if (2*i) + 1 < len(arr) and arr[i] < arr[(2*i) + 1] and arr[(2*i) + 1] >= arr[2*i]:

                temp = arr[i]
                arr[i] = arr[(2*i) + 1]
                arr[(2*i) + 1] = temp

                i = (2*i) + 1

            elif arr[i] < arr[(2*i)]:

                temp = arr[i]
                arr[i] = arr[(2*i)]
                arr[(2*i)] = temp

                i = (2*i)

            else:
                break

        return arr

    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [0]
        heap.append(stones[0])

        for i in range(1,len(stones)):

            heap = self.push(heap,stones[i])

        while len(heap) > 2:

            x = heap[1]
            heap = self.pop(heap)

            y = heap[1]
            heap = self.pop(heap)

            if x!=y:
                self.push(heap,abs(x-y))

        return heap[-1]
