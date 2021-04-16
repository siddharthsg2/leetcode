# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        if p.val!=q.val:
            return False
        
        l=self.isSameTree(p.left,q.left)
        r=self.isSameTree(p.right,q.right)
        return l & r
