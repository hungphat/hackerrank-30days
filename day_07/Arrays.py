f  = open('input.txt', 'r')
wr = open('output.txt', 'w')


class Array:
    def __init__(self, list):
        self.input_array = list

    def reverse_array(self, range):
        input_list = self.input_array
        split_array = []
        for i in input_list:
            split_array.extend(i.split())
        array_reverse = split_array[0:range]
        array_reverse.reverse()
        for j in array_reverse:
            wr.write(j+ ' ')

n = int(f.readline())
d = []
for i in f:
    read = i.strip()
    d.append(read)          # TODO what are you doing here? If you want to get the array, why you dont use
                            #  *arr = list(map(int, input().rstrip().split()))* from HKR website ?
Array(d).reverse_array(n)

# TODO no need to use class