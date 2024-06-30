class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0

        for nums in digits:
            number = number * 10 + nums

        number += 1

        digits = []

        while(number > 0):
            last_digit = number % 10

            if(len(digits) == 0):
                digits.append(last_digit)
            else:
                digits.insert(0,last_digit)
            number = number // 10

        return digits



