class Solution:
    temp = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n not in self.temp:
                self.temp[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.temp[n]
