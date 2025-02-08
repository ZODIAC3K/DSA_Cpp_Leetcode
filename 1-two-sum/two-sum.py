class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # function name: twoSum
        # nums is a list of integers
        # target is an integer
        # return a list of integers

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i] + nums[j] == target):
        #             return [i, j]
        
        # return []
        result = []
        data = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in data:
                result.append(i)
                result.append(data[diff])
                return result
            data[v] = i
        
        return result
                 
        