def run(input, output):
    class Difference:
        def __init__(self, a):
            self.__elements = a

        # Add your code here
        def computeDifference(self):
            list_compute = []
            arr = self.__elements
            self.maximumDifference = max(arr) - min(arr)



    # End of Difference class

    f = open(input, 'r')
    wr = open(output, 'w')
    a = [int(e) for e in f.readline().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)
if __name__ == '__main__':
    run('input.txt', 'output.txt')