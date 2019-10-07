f  = open('input.txt', 'r')
wr = open('output.txt', 'w')
class Customer:
    def __init__(self,array):
        self.array = array

    def phone_list(self,n):
        array = self.array
        phone_list = []
        query_name = []
        list = 0
        for i in array:
            if list < n :
                phone_list.append(i.split())
            if list >= n:
                query_name.append(i.split())
            list += 1
        for j in range(n):
            if phone_list[j][0] == query_name[j][0]:
                print(f'{query_name[j][0]}={phone_list[j][1]}')
            else:
                print('Not found')


a = int(f.readline())
Customer(f).phone_list(a)
