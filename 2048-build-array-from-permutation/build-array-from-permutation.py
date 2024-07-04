class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        vec = []
        for i in range(len(nums)):
            vec.append(nums[nums[i]])
        return vec