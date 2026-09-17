# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def helper(node, d):
            if not node:
                return None
            if len(res) == d:
                res.append([])

            res[d].append(node.val)
            helper(node.left, d+1)
            helper(node.right, d+1)
        helper(root,0)
        return res
        