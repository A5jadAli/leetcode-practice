# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            self.result.append(node.val)
            inorder(node.right)

        inorder(root)
        return self.result[k-1]

        '''inorder traversal will give us sorted array
           and then we can return kth element from that array'''
        