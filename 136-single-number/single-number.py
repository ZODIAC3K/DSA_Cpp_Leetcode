class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for e in nums:
            hashmap[e] = hashmap.get(e,0) + 1
        
        for key, value in hashmap.items():
            if value == 1:
                return key

        