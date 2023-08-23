class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = set()  # Creating an empty set
        strs = sorted(strs)  # Sorting the input list
        
        for i in range(len(strs)):
            # Convert each string to a sorted list of characters
            sorted_str = ''.join(sorted(strs[i]))
            hashset.add(sorted_str)  # Adding sorted string to the set
        
        # Initialize a dictionary to store anagrams
        anagram_dict = {sorted_str: [] for sorted_str in hashset}
        
        # Populate the anagram dictionary
        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            anagram_dict[sorted_str].append(strs[i])
        
        # Extract values (lists of anagrams) from the dictionary
        returnList = list(anagram_dict.values())
        return returnList
