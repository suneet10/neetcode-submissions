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

        
        if len(self.heap)-1 >= self.tar:
            # print(self.heap)
            return self.heap[0-self.tar]
        return