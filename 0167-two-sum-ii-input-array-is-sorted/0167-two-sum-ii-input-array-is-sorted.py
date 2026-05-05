class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_a = 0
        pointer_b = len(numbers) - 1
        
        while pointer_a < pointer_b:
            current_sum = numbers[pointer_a] + numbers[pointer_b]
            
            if current_sum == target:
                return [pointer_a + 1, pointer_b + 1]  # Convert to 1-indexed
            elif current_sum < target:
                pointer_a += 1  # Need a larger sum
            else:
                pointer_b -= 1  # Need a smaller sum
        
        return None  # No solution found
