class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        
        # Make a number from given digits
        for nums in digits:
            number = number * 10 + nums

        # Added a 1 to the number
        number += 1

        # Didn't want to use extra space for array so used "digits" (by default array is passed by reference) by make it empty
        digits = []

        # read last digit from number using "number % 10" and pushed in simple in digits if the len of digits is 0 else inserted it in front of digits and then removed last digit from number using "number // 10" and return the new digits

        while(number > 0):
            last_digit = number % 10

            if(len(digits) == 0):
                digits.append(last_digit)
            else:
                digits.insert(0,last_digit)
            number = number // 10

        return digits



