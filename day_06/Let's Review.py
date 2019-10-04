f  = open('..//Input-Output//input.txt', 'r')
wr = open('..//Input-Output//output.txt', 'w')
d = []
class array:
    def __init__(self, rang):
        #self.inter = n
        self.rang  = rang


    def Arrange(self,line):
        i=0
        r = self.rang
        for a in r:
            e = list(a)
            r = str("".join(map(str, e[0::line])))
            z = str("".join(map(str, e[1::line])))
            wr.write(f'{r +" "+  z} \n')


a=int(f.readline())
n = 0
for i in f:
    read = i.strip()
    d.append(read)
array(d).Arrange(a)






