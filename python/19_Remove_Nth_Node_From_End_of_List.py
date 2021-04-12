# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count=0
        p=head
        q=head
        while q!=None:
            if(count<=n):
                q=q.next
            else:
                p=p.next
                q=q.next
            count+=1
        if(count==n):
            head=head.next
        else:
            p.next=p.next.next
    
        return head
