# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1=""
        n2=""
        while(l1):
            n1=n1+str(l1.val)
            l1=l1.next
        while(l2):
            n2=n2+str(l2.val)
            l2=l2.next
        ans=int(n1)+int(n2)
        ans=str(ans)
        a=[]
        for i in ans:
            a.append(ListNode(i))
        head=a[0]    
        for j in range(len(a)):
            if(j==len(a)-1):
                a[j].next=None
            else:
                a[j].next=a[j+1]
        return head
