from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store sorted word as key and list of anagrams as value
        anagrams = {}
        
        for word in strs:
            # Sort the word and use it as a key
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []
            anagrams[sorted_word].append(word)
        
        # Return the values of the dictionary as a list of lists
        return list(anagrams.values())
