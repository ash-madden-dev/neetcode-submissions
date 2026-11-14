class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] != sorted_nums[i + 1] - 1:
                return False
        return True
