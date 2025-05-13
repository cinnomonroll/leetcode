# Given the root of a binary tree, invert the tree, and return its root.
# Example:
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# 
# Input: root = [2,1,3]
# Output: [2,3,1]
# 
# Input: root = []
# Output: []

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
# take a tree and invert it using DFS 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root

def print_tree(root):
    if not root:
        return None
    print(root.val, end = ' ')
    print_tree(root.left)
    print_tree(root.right)


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    sol = Solution()
    print_tree(sol.invertTree(root))
    