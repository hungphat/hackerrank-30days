import sys
from collections import deque

# Write your code here
def run(input, output):
    class Solution:
        def __init__(self):
            self.queue = deque()
            self.stack = list()

        def pushCharacter(self,input_string):
            self.stack.append(input_string)
            pass
        def dequeueCharacter(self):
            return self.queue.popleft()
            pass
        def enqueueCharacter(self,input_string):
            self.queue.append(input_string)
            pass
        def popCharacter(self):
            return self.stack.pop()
            pass

    # read the string s
    f = open(input, 'r')
    wr = open(output, 'w')
    s =f.readline()
    # Create the Solution class object
    obj = Solution()

    l = len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])

    isPalindrome = True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    '''
    for i in range(l // 2):
        if obj.popCharacter() != obj.dequeueCharacter():
            isPalindrome = False
            break
    # finally print whether string s is palindrome or not.
    if isPalindrome:
        print("The word, " + s + ", is a palindrome.")
    else:
        print("The word, " + s + ", is not a palindrome.")
if __name__ == '__main__':
    run('input.txt', 'output.txt')