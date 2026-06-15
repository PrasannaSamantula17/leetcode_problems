# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        curr = nums[0]
        for i in nums[1:]:
            curr = max(i,curr+i)
            
            if curr > best:
                best = curr
        return best
