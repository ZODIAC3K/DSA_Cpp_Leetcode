class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings. If they are anagrams, their sorted forms will be identical else they will differ. But sorting returns a list which requires extra space that makings this approach sub-optimal.
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False
        