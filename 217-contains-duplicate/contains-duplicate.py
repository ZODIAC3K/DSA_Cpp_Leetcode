class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # saw = set()
        # for e in nums:
        #     if e in saw:
        #         return True
        #     saw.add(e)
        # return False

        saw = {}
        for e in nums:
            if e in saw:
                return True
            saw[e] = saw.get(e, 0) + 1
        return False