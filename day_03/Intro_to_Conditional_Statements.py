def run(input, output):
    f  = open(input, 'r')
    wr = open(output, 'w')
    for a in f:
        c = a.strip()
        try:
            int(c)
            e = int(c)
            if e % 2 != 0:
                wr.write('Weird\n')
            if e >= 2 and e <= 5 and e % 2 == 0:
                wr.write('Not Weird\n')
            if e >= 6 and e <= 20 and e % 2 == 0:
                wr.write('Weird\n')
            if e > 20 and e % 2 == 0:
                wr.write('Not Weird\n')
        except ValueError:
            wr.write('Chi xet so nguyen \n')
    wr.close()
if __name__ == '__main__':
    run('input.txt','output.txt')