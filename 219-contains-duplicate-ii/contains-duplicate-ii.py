class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create hset for storing previous of k elements...
        hset = {}
        # Traverse for all elements of the given array in a for loop...
        for idx in range(len(nums)):
            # If current element duplicate is present and their index is less than k return true
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
        # If no duplicate element is found whose value is less idx and hset[nums[idx]]then return false...
        return False
        
        