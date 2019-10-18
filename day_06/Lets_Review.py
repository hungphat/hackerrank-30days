def run(input, output):
    class array:
        def __init__(self, rang):
            #self.inter = n
            self.rang  = rang

        def Arrange(self,line):  # TODO do NOT capital first letter function in
            r = self.rang
            for a in r:
                e = list(a)
                l = str("".join(map(str, e[0::line]))) #--Combine inside List to 1 string
                z = str("".join(map(str, e[1::line])))
                wr.write(f'{l +" "+ z}\n')

    f  = open(input,  'r')
    wr = open(output, 'w')
    a  = int(f.readline())
    d  = []
    for i in f:
        read = i.strip()
        d.append(read)
    array(d).Arrange(a)
    wr.close()
if __name__ == '__main__':
    run('input.txt', 'output.txt')








