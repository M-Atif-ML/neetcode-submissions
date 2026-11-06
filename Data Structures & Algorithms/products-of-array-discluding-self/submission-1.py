class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        prefix[1] = 1
        suffix[n-1] = 1
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
            # suffix[n-i] = suffix[n-i] * nums[n-i]
        for i in range(n-2,-1,-1):
            
            suffix[i] = suffix[i+1] * nums[i+1]
        

        return [suffix[i]*prefix[i] for i in range(n)]