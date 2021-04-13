# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        def recur(root, ans):
            if root:
                recur(root.left,ans)
                ans.append(root.val)
                recur(root.right,ans)
        recur(root,ans)
        return ans
