class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        while numbers[i]+numbers[n-1] != target:
            if numbers[i]+numbers[n-1] > target:
                n -= 1
            else:
                i+=1
        return [min(n,i)+1,max(n,i)]


