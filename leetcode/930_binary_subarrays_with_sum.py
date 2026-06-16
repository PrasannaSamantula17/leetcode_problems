# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}  # Frequency of prefix sums
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            current_sum += num
            
            # If (current_sum - goal) has been seen, add its frequency
            if (current_sum - goal) in count:
                total_subarrays += count[current_sum - goal]
            
            # Record the current_sum in the map
            count[current_sum] = count.get(current_sum, 0) + 1
            
        return total_subarrays
