from collections import defaultdict  # Creates a dictionary with automatic empty lists.


class Solution:  # LeetCode-style class wrapper.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # Receives a list of words and returns grouped anagrams.
        groups = defaultdict(list)  # Stores words by their sorted-letter key.

        for word in strs:  # Look at each word one by one.
            key = ''.join(sorted(word))  # Sort letters so anagrams produce the same key.
            groups[key].append(word)  # Add the word to its matching group.

        result = list(groups.values())  # Convert the grouped values into a normal list.
        print(result)  # Show the grouped anagrams.
        return result  # Return the grouped anagrams.