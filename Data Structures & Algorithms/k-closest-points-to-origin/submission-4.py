import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        
        for i in points:
            s = ((i[0]**2)+(i[1]**2))
            i = [s,i]

            if len(heap) < k:
                heapq.heappush_max(heap,i)

            else:
                if (i[0]) < (heap[0][0]):
                    heapq.heappop_max(heap)
                    heapq.heappush_max(heap,i)
            # print(heap)
        # print(points)
        ans = []

        for i in heap:
            ans.append(i[1])

        return ans