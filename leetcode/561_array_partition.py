# Time Complexity - O(n log n)
# Space Complexity - O(1) or O(n)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
