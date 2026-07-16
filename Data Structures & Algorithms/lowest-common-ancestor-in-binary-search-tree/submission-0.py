# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # common_l = []
        # common_r = [root]
        # p_found = False
        # q_found = False
        # queue = deque()
        # queue.append(root)
        # while len(queue) > 0:
        #     v = deque()
        #     node = queue.popleft()
        #     print(node.val)
        #     if q_found and p_found:
        #         break            
        #     if node.left:
        #         v.append(node.left)
        #         common_l.append(node)
        #     if node.right:
        #         v.append(node.right)
        #         common_r.append(node)
        #     for neighbor in v:
        #         queue.append(neighbor)
        while True:

            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root

        # print([common.val for common in common_l]) 
        # print([common.val for common in common_r]) 
