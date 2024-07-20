class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]
        
        count = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if lower <= sums[j] - sums[i] <= upper:
                    count += 1
        
        return count