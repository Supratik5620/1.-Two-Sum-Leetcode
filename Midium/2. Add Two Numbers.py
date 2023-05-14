# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Initialize variables
        carry = 0  # Stores the carry value when summing digits
        dummy = ListNode(0)  # Dummy node to simplify the logic
        curr = dummy  # Pointer to the current node in the result list

        # Iterate until both input lists and the carry value are exhausted
        while l1 or l2 or carry:
            # Get the values of the current digits from l1 and l2 (or 0 if any of them is exhausted)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Compute the sum of the digits and the carry value
            sum_val = x + y + carry
            carry = sum_val // 10  # Determine the new carry value

            # Create a new node with the units digit of the sum and append it to the result list
            curr.next = ListNode(sum_val % 10)

            # Move the current pointers to the next nodes in the input lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # Move the current pointer in the result list to the newly appended node
            curr = curr.next

        # Return the head of the resulting linked list (excluding the dummy node)
        return dummy.next
