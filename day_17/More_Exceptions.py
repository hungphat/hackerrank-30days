def run(input, output):
    class Calculator:
        def power(self, n, p):
            if n < 0 or p < 0 :
                return Exception("n and p should be non-negative")
            else:
                return pow(n, p)

    f = open(input, 'r')
    wr = open(output, 'w')
    myCalculator=Calculator()
    T=int(f.readline())
    for i in range(T):
        for j in f:
            n,p = map(int, j.split())
            try:
                ans=myCalculator.power(n,p)
                print(ans)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    run('input.txt', 'output.txt')