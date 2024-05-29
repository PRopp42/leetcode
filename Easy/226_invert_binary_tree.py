"""
https://leetcode.com/problems/invert-binary-tree
Given the root of a binary tree, invert the tree, and return its root.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Graph problems always make me happy. We can use a cute little recursive 
        function that traverses the tree and flips everything around.
        There are some modifications to make this faster, at the cost of readability.
        """
        if not root: # If we get nothing, we give nothing.
            return root

        root.left, root.right = root.right, root.left # 🎵 Do the Hokey Pokey 🎵

        self.invertNode(root.left) # Recursive call left
        self.invertNode(root.right) # Then right

        return root

"""
Analysis:
We need to touch every node once, O(n)
"""