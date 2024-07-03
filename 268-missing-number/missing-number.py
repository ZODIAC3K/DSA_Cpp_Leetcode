class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # TC --> O(n*logn)

        #edge case
        if len(nums) == 1:
            if nums[0] == 1:
                return 0
            
            if nums[0] == 0:
                return 1

        max_range = len(nums)

        nums.sort()
        #edge case
        if nums[0] != 0:
            return 0

        for i in range(1,max_range):
            if nums[i] - nums[i-1] != 1:
                return nums[i] - 1
        
        return max_range
        