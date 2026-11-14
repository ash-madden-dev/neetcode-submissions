class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            print("Failed 1")
            return False
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] != sorted_nums[i + 1] - 1:
                return False
        return True
