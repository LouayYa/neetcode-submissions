# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head != None:
            stack.append(head.val)
            head = head.next
        
        dummy = ListNode(0)
        curr = dummy
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next
        
        return dummy.next