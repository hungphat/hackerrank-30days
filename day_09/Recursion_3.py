f  = open('input.txt', 'r')
wr = open('output.txt', 'w')

a = int(f.readline())
z=1
for i in range(1,a+1):
   z= z*i
wr.write(str(z))