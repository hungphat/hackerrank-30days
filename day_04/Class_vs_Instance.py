def run(input, output):
    f  = open(input, 'r')
    wr = open(output, 'w')
    d = []
    e = []
    class Person:
        def __init__(self,initialAge):
            self.inittia_age = initialAge
            if self.inittia_age < 0:
                wr.write('Age is not valid, setting age to 0\n')
        def amIOld(self):
            compte = self.inittia_age
            if compte>=0 and compte < 13 :
                wr.write('You are young.\n')
            if compte >=13 and compte < 18:
                wr.write('You are teenager.\n')
            if compte >=18:
                wr.write('You are old.\n')
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
        wr.write('\n')
    for j in g:
        customer = Person(j)
        customer.amIOld()
        customer_yp = customer.yearPasses()
        Person(customer_yp).amIOld()
        wr.write('\n')
    wr.close()
if __name__ == '__main__':
    run('input.txt', 'output.txt')

