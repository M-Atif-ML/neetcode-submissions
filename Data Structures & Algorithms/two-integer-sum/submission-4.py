class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        temp = []

        for ind,num in enumerate(nums):
            temp.append([ind,num]) # this part is important because we have to save the actual indices before sorting otherwise the output will return the indices of sorted array which wont be correct

        temp.sort(key=lambda x: x[1])

        i,j = 0,len(nums)-1

        while i<j:
            curr = temp[i][1]+temp[j][1]
            # print(f"indices: {i,j}, sum: {nums[i]+nums[j]}")

            if curr == target:
                return [min(temp[i][0],temp[j][0]),max(temp[i][0],temp[j][0])]
            elif curr < target:
                i += 1
            else:
                j-=1
        return []
        