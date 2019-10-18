import sys

class Node:
    def __init__(self, data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root, data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left, data)
                root.left=cur
            else:
                cur=self.insert(root.right, data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = [root]
        for i in queue:
            print(i.data, end=" ")
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)

T=6
S=[3,5,4,7,2,1]
myTree=Solution()
root=None
for i in range(T):
    for j in S:
        data=j
        root=myTree.insert(root, data)
myTree.levelOrder(root)
