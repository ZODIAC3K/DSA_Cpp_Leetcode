from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings. If they are anagrams, their sorted forms will be identical else they will differ. But sorting returns a list which requires extra space that makings this approach sub-optimal.
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # else:
        #     return False
        
        # Dictionary with Counter Approach
        # return Counter(s) == Counter(t)
        
        # Normal Dictionary Implementain
        if len(s) != len(t):  # Anagrams must have the same length
            return False
        
        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for char in t:
            if char in char_count:
                if char_count.get(char, 0) == 0: # "if char_count[char] < 0:" this would give error if char is not presnet in dict which is not something we want
                    return False
                char_count[char] -= 1
            else:
                return False
        
        return True