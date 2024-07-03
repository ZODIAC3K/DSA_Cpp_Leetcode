class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap = {}
        # for element in nums:
        #     hashmap[element] = hashmap.get(element, 0) + 1
        
        # for key, value in hashmap.items():
        #     if value > len(nums)/2:
        #         return key

        ###
        ### OR
        ###

        nums.sort()
        n = len(nums)
        return nums[n//2] # because when we sort we will see at n//2 index there is that element which has accured more than n/2 time where n is the len of of the given array.