# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        

        slow = prev
        slow2 = head

        ans = float('-inf')

        while slow and slow2:
            ans = max(ans, slow.val + slow2.val)
            slow = slow.next
            slow2 = slow2.next

        return ans
