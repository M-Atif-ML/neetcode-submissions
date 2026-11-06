class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap =defaultdict(int)
   
        for num in nums:
            hashmap[num] += 1
        temp=[]
     
        for key in hashmap:
            temp.append((-hashmap[key],key))

        heapq.heapify(temp)
        
        return [heapq.heappop(temp)[1] for _ in range(k)]

