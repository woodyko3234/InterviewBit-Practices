# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        stack=[]
        if root :
            stack.append(root)
        while stack:
            popping=[]
            while stack:
                node=stack.pop()
                if stack:
                    node.next=stack[-1]
                if node.left:
                    popping.append(node.left)
                if node.right:
                    popping.append(node.right)
            stack=popping[::-1]
        return root
