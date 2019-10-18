def run(input, output):
   f  = open(input, 'r')
   wr = open(output, 'w')

   a = int(f.readline())
   z=1
   for i in range(1, a+1):
      z= z*i
   wr.write(f'{z}\n')
if __name__ == '__main__':
    run('input.txt', 'output.txt')