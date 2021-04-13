# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def cutinhalf(head):
    slow, fast=head, head.next
    if not fast:
        return head
    while fast.next and fast.next.next:
        prev=slow
        slow=slow.next
        fast=fast.next.next
    if fast.next:
        slow=slow.next
        fast=fast.next
    p=slow.next
    slow.next=None
    return p
def rev(head):
    prev = None
    while head is not None:
        nextnode = head.next
        head.next = prev
        prev = head
        head = nextnode
    return prev
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head.next==None:
            return head
        l2=cutinhalf(head)
        l2=rev(l2)
        l1=head
        while l1 is not None and l2 is not None:
            temp=l1.next
            l1.next=l2
            l2=l2.next
            l1=l1.next
            l1.next=temp
            l1=l1.next
