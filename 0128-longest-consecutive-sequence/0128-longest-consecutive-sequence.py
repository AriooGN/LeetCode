class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        
        # Convert the input list to a set for efficient presence checks
        nums_set = set(nums)
        longest_streak = 0
        
        # Iterate through each number in the set
        for num in nums_set:
            # If the predecessor of the current number is not in the set
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                # Iterate forward to find consecutive numbers
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak if the current streak is larger
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
