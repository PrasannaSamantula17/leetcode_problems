# Time Complexity - O(n)
# Space Complexity - O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            current_sum = numbers[i] + numbers[j]
            
            if current_sum == target:
                return [i + 1, j + 1]
            elif current_sum < target:
                i += 1  # Need a larger sum
            else:
                j -= 1  # Need a smaller sum
