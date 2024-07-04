class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        r = 0
        no1 = 0

        while r < len(nums):
            if nums[r] == 1:
                no1 = max(no1, r - l + 1)
            else:
                while nums[l] == 1:
                    l += 1
                l += 1
            r += 1

        return no1
        