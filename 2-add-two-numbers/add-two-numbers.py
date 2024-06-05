# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_val = 0
        l2_val = 0
        counter = 0

        while l1:
            l1_val += l1.val * (10 ** counter)
            counter += 1
            l1 = l1.next

        counter = 0
        while l2:
            l2_val += l2.val * (10 ** counter)
            counter += 1
            l2 = l2.next

        sum_val = l1_val + l2_val

        dummy = ListNode(0)
        linker = dummy

        if sum_val == 0:
            return ListNode(0)

        while sum_val != 0:
            last_digit = sum_val % 10  # getting last digit
            sum_val //= 10  # removing last digit
            curr_node = ListNode(last_digit)
            linker.next = curr_node
            linker = linker.next

        return dummy.next
        