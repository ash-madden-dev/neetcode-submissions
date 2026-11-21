class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ints = {}
        lucky_nums = [-1]

        for num in arr:
            if num in ints:
                ints[num] += 1
            else:
                ints[num] = 1
        
        for key, val in ints.items():
            if key == val and key > lucky_nums[-1]:
                lucky_nums.append(key)
        
        return lucky_nums[-1]