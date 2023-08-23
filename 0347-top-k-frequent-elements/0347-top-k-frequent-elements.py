class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Check if the length of nums is equal to k
        if len(nums) == k:
            return nums
        # Check if k is 0
        elif k == 0:
            return

        # Create a set to store unique numbers
        numsSet = set()

        # Add each number in nums to the set
        for i in range(len(nums)):
            numsSet.add(nums[i])
        
        # Create a dictionary with numbers as keys and initial count as 0
        nums_dic = {number: 0 for number in numsSet}

        # Count the frequency of each number and update the dictionary
        for i in range(len(nums)):
            nums_dic[nums[i]] += 1

        # Convert the dictionary items to a list of key-value pairs
        nums_dic = [[key, value] for key, value in nums_dic.items()]

        # Sort the list based on the frequency in descending order
        nums_dic = sorted(nums_dic, key=lambda item: item[1], reverse=True)
        
        # Create a list to store the top k frequent numbers
        returnList = []
        
        # Add the top k frequent numbers to the returnList
        for i in range(0, k):
            returnList.append(nums_dic[i][0])
        
        # Return the list of top k frequent numbers
        return returnList
