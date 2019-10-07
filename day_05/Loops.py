f  = open('input.txt', 'r')
wr = open('output.txt', 'w')
d = []

class compute:
    def __init__(self,num):
        self.num = num
    def multiples(self):
        for i in range(1,11):
           wr.write(str(f'{self.num * i} \n'))
a = int(f.readline())
compute(a).multiples()

#TODO Phat vi sao phai luon viet 1 class, minh co the chi can khai bao' ham multiples() tr.tiep
