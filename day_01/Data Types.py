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

#TODO Phat cuoi tep chi co du'ng 01 dong tra'ng

#TODO Phat chay bi loi
# Traceback (most recent call last):
#   File "/home/namgivu/NN/code/_gigacover_/_personal_/phat/hackerrank-30days/day_01/Data Types.py", line 12, in <module>
#     wr.write(f'{int(int(d[0]) + float(d[1]))} \n')
# ValueError: invalid literal for int() with base 10: 'Hacker'
