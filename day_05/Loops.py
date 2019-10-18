def run(input, output):
    f  = open(input, 'r')
    wr = open(output, 'w')
    d = []
    def multiples(b):
        for i in range(1,11):
            wr.write(str(f'{b} x {i} = {b * i}\n'))
    a = int(f.readline())
    multiples(a)
    wr.close()

if __name__ == '__main__':
    run('input.txt', 'output.txt')

