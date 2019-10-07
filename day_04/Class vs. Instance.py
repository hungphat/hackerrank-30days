f  = open('..//Input-Output//input.txt', 'r')
wr = open('..//Input-Output//output.txt', 'w')
d = []
e = []
g = []
class Person:
    def __init__(self,initialAge):
        self.inittia_age = initialAge
        if self.inittia_age < 0:
            print('Age is not valid, setting age to 0')
    def amIOld(self):
        compte = self.inittia_age
        if compte>=0 and compte < 13 :
            print('You are young.')
        if compte >=13 and compte < 18:
            print('You are teenager.')
        if compte >=18:
            print('You are old.')
    def yearPasses(self):
        return self.inittia_age + 3

for line in f:
    a = int(line.strip())
    e.append(a)
    if a < 0:
        d.append(a)
g = [x for x in e if x not in d]        #--Remove e from d
for z in d:
    customer_under0 = Person(z)
    customer_under0.amIOld()
    customer_under0_yp = customer_under0.yearPasses()
    Person(customer_under0_yp).amIOld()
    print('\n')
for j in g:
    customer = Person(j)
    customer.amIOld()
    customer_yp = customer.yearPasses()
    Person(customer_yp).amIOld()
    print('\n')

#TODO Phat em dat ten bien co' y nghia hon, tranh' viec dat ten theo bang chu cai abcdefg
