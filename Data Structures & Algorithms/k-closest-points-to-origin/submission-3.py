import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        
        for i in points:
            
            i.append((i[0]**2)+(i[1]**2))

            if len(heap) < k:
                heapq.heappush_max(heap,i)

            else:
                if i[2] < heap[0][2]:
                    heapq.heappop_max(heap)
                    heapq.heappush_max(heap,i)
        
        for i in heap:
            i.pop()
        return heap