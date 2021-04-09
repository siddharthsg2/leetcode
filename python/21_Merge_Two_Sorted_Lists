# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(-1)
        p=head
        while l1 and l2:
            if l1.val<=l2.val:
                p.next=l1
                l1=l1.next
            elif l2.val<l1.val:
                p.next=l2
                l2=l2.next
            
            p=p.next
        p.next=l1 if l1 else l2
        head=head.next
        return head
