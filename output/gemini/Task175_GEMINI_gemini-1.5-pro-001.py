class MountainArray:
    def __init__(self, array):
        self.array = array

    def get(self, index: int) -> int:
        return self.array[index]

    def length(self) -> int:
        return len(self.array)
      
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
        index = self.binary_search(mountain_arr, target, 0, peak, True)
        if index != -1:
            return index
        return self.binary_search(mountain_arr, target, peak + 1, n - 1, False)

    def binary_search(self, mountain_arr, target, left, right, ascending):
        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif (mid_val < target and ascending) or (mid_val > target and not ascending):
                left = mid + 1
            else:
                right = mid - 1
        return -1