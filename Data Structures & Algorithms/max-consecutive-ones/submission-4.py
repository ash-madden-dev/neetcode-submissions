class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0
        for num in nums:
            if num:
                count += 1
            else:
                if count > maximum:
                    maximum = count
                count = 0
        return max(maximum, count)