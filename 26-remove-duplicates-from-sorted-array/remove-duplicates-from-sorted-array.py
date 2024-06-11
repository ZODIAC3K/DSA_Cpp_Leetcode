class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        last = None
        for n in nums:
            if n == last: continue
            last = n
            nums[cur] = n
            cur += 1
        return cur
        