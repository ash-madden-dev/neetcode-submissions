class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        for i in range(length):
            if i == length - 1:
                arr[-1] = -1
                break
            else: 
                greatest_element = max(arr[i+1:])
                arr[i] = greatest_element
        return arr
