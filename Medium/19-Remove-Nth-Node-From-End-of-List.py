# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = n
        npointer = head
        dummy = ListNode(0, head)
        while count and npointer:
            npointer = npointer.next
            count -= 1
        
        lpointer = dummy
        while npointer:
            npointer = npointer.next
            lpointer = lpointer.next
            

        lpointer.next = lpointer.next.next
        
        return dummy.next
        
