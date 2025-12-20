class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for value in nums:
            if value == 0:
                nums.remove(value) # gets index and remove the value and return the value.
                nums.append(value)
            else:
                continue
                

        