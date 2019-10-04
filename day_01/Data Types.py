f  = open('..//Input-Output//input.txt', 'r')
wr = open('..//Input-Output//output.txt', 'w')
n = 0
d = []
s ='Hacker rank'


for a in f:
    c = a.strip()
    d.append(c)

wr.write(f'{int(int(d[0]) + float(d[1]))} \n')
wr.write(f'{float(d[1]) + float(d[1])}  \n ')
wr.write(f'{s} {d[2]}')
wr.close()

