class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        size = len(nums)

        for i in range(size):
            complement = target - nums[i]
            if complement in numsMap:
                return [numsMap[complement], i]
            numsMap[nums[i]] = i

        return []  # No solution found