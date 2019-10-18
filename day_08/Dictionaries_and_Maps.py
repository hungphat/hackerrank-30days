def run(input, output):
    f  = open(input, 'r')
    wr = open(output, 'w')
    class Customer:
        def __init__(self, array):
            self.array = array

        def phone_list(self, n):
            array = self.array
            phone_list = []
            query_name = []
            list = 0               # TODO list is the built-in function name, dont use this for variable
            for i in array:
                if list < n :
                    phone_list.append(i.split())
                if list >= n:
                    query_name.append(i.split())
                list += 1
            for j in range(n):
                if phone_list[j][0] == query_name[j][0]:
                    wr.write(f'{query_name[j][0]}={phone_list[j][1]}\n')
                else:
                    wr.write('Not found\n')


    a = int(f.readline())
    Customer(f).phone_list(a)
    wr.close()
if __name__ == '__main__':
    run('input.txt', 'output.txt')