class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        result = [0]*n
        result[0]=cost[0]
        result[1]=cost[1]

        
        for i in range(2,n):
            result[i] = min(result[i-1],result[i-2])+ cost[i]
        return min(result[n-1],result[n-2])
            