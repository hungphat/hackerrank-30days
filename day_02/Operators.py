def meal_compute(meal, tip, tax):
    tip_cost = meal * (tip / 100)
    tax_cost = meal * (tax / 100)
    total_cost = meal + tax_cost + tip_cost
    return int(total_cost)

def run(input, output):
    f  = open(input, 'r')
    wr = open(output, 'w')
    d = []
    for a in f:
        c = a.strip()
        d.append(c)

    meal_cost   = float(d[0])
    tip_percent = int  (d[1])
    tax_percent = int  (d[2])

    #---Print Output
    round_cost = meal_compute(meal_cost, tip_percent, tax_percent)
    wr.write(f'{round_cost}\n')
    wr.close()

if __name__ == '__main__':
    run('input.txt','output.txt')