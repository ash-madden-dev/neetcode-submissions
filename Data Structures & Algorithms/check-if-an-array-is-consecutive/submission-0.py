class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        return len(nums) == len(set(nums))