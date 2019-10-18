class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root:
            left = 0
            right = 0
            if root.left:
                left = 1 + self.getHeight(root.left)
            if root.right:
                right = 1 + self.getHeight(root.right)
            return max(left, right)
        else:
            return 0
        #Write your code here

T=7
S=[3,5,2,1,4,6,7]
myTree=Solution()
root=None
for i in range(T):
    for j in S:
        data=j
        root=myTree.insert(root,data)
height = myTree.getHeight(root)
print(height)
