class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, current_num in enumerate(nums):
            if target - current_num in hash_map:
                return sorted([index, hash_map[target - current_num]])
            else:
                hash_map[current_num] = index

            
        