class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for point in points:
            dist.append((math.sqrt(point[0]**2+point[1]**2),point))
        heapq.heapify(dist)

        result =[]

        for i in range(k):
            result.append(heapq.heappop(dist)[1])

        print(result)
        return result 