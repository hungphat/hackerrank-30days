def run(input, output):
    f  = open(input, 'r')
    wr = open(output, 'w')
    d = []
    arr =[]
    i=0
    hourglass_sum = 0       # TODO redundant variable
    for k in f:
        arr.append(list(map(int, k.rstrip().split(' '))))
    for i in range(len(arr)-2):     # TODO the matrix is 6x6, so you can you range(4)
        for j in range(len(arr[i])-2):
            hourglass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            d.append(hourglass_sum)
    print(max(d))

if __name__ == '__main__':
    run('input.txt', 'output.txt')
