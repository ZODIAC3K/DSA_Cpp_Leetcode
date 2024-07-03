class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for element in nums:
            hashmap[element] = hashmap.get(element, 0) + 1
        
        for key, value in hashmap.items():
            if value > len(nums)/2:
                return key