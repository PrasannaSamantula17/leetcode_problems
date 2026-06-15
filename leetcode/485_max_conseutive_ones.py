# Time Complexity - O(n)
# Space Complexity - O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        record = 0
        i = 0
        count = 0
        while(i<len(nums)):
            if nums[i] == 1:
                count += 1
                if count > record:
                    record = count
            else:
                count = 0
            i += 1
        return record
