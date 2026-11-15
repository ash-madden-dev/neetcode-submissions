class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        digits = list(str(sorted(nums)[0]))
        sum = 0
        for digit in digits:
            sum += int(digit)
        if sum % 2 == 0:
            return 1
        else:
            return 0
        
