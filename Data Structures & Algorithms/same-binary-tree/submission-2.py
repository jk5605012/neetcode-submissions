# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = []
        q_list = []

        def rec(ll, list_v):
            if not ll:
                return
            list_v.append(ll.val)
                
            if ll.left:
                rec(ll.left, list_v)
            if ll.right and not ll.left:
                list_v.append(None)
            if ll.right:
                rec(ll.right, list_v)
        
        rec(p, p_list)
        rec(q, q_list)
        print(p_list)
        print(q_list)
        if p_list != q_list:
            return False
        return True

