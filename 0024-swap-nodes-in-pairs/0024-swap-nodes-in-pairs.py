# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while slow and fast:
            slow.val, fast.val = fast.val, slow.val

            if not fast.next or not fast.next.next:
                break

            slow = fast.next
            fast = slow.next
        
        return head


