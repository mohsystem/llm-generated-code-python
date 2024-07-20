class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        return self.reversePairs(left) + self.reversePairs(right) + self.mergeAndCount(left, right)
    
    def mergeAndCount(self, left: List[int], right: List[int]) -> int:
        n1 = len(left)
        n2 = len(right)
        merged = [0] * (n1 + n2)
        i = j = k = 0
        count = 0
        while i < n1 and j < n2:
            if left[i] > 2 * right[j]:
                count += n1 - i
                j += 1
            else:
                i += 1
        while i < n1:
            merged[k] = left[i]
            i += 1
            k += 1
        while j < n2:
            merged[k] = right[j]
            j += 1
            k += 1
        return count