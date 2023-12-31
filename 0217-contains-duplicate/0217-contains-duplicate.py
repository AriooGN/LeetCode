class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(nums) <= 1):
            return False
        
        nums.sort()
        for i, num in enumerate(nums):
            if(num == nums[i-1]):
                return True
        
        return False
        
