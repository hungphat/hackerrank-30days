def run(input, output):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


    class Solution:
        def display(self, head):
            current = head
            while current:
                print(current.data, end=' ')
                current = current.next

        def insert(self, head, data):
            newNode = Node(data)
            if not head:
                return newNode
            current = head
            while current.next:
                current = current.next
            current.next = newNode
            return head




    # Complete this method

    f = open(input, 'r')
    wr = open(output, 'w')
    mylist = Solution()
    T = int(f.readline())
    head = None
    for i in range(T):
        for j in f:
            data = j.rstrip()
            head = mylist.insert(head, data)
    mylist.display(head)

if __name__ == '__main__':
    run('input.txt', 'output.txt')