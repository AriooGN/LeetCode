class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        return Counter(nums) != Counter(nums_set)