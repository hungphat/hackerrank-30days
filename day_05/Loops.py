f  = open('..//Input-Output//input.txt', 'r')
wr = open('..//Input-Output//output.txt', 'w')
d = []

class compute:
    def __init__(self,num):
        self.num = num

    def multiples(self):
        for i in range(1,11):
           print(self.num * i)
a = int(f.readline())
compute(a).multiples()