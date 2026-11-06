class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        for i in range(length):
            if i != length - 1:
                greatest_element = max(arr[i+1:])
                arr[i] = greatest_element
            else:
                arr[-1] = -1
        return arr
