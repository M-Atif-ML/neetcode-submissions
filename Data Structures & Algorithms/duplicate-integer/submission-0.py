class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_ = set()

        for i in nums:
            set_.add(i)

        return len(set_) != len(nums)