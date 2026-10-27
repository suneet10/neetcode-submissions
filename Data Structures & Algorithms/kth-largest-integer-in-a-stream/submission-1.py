class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.tar = k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        self.heap.append(val)
        i = len(self.heap)-1
        while i > 1 and self.heap[i] < self.heap[i//2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = temp

            i = i//2 

        
        if len(self.heap)-1 > self.tar:
            if len(self.heap) == 2:
                return self.heap.pop()
            
            self.heap[1] = self.heap.pop()
            i = 1

            while (2*i) < len(self.heap):

                if (2*i) + 1 < len(self.heap) and self.heap[(2*i) + 1] < self.heap[i] and self.heap[(2*i)+1] <= self.heap[2*i]: #if a right child exists and the right child is less that the root node and then right child is less than or equal to the left child, we do a right and node swap and update i

                    temp = self.heap[i]
                    self.heap[i] = self.heap[(2*i)+1]
                    self.heap[(2*i)+1] = temp

                    i = (2*i)+1

                elif self.heap[(2*i)] < self.heap[i]: #elif that left child is less that the node, we do a left swap and update i

                    temp = self.heap[i]
                    self.heap[i] = self.heap[(2*i)]
                    self.heap[(2*i)] = temp

                    i = (2*i)

                else: 
                    break
            
            return self.heap[1]


