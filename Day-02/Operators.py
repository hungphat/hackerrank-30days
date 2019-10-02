f  = open('..//Input-Output//input.txt', 'r')
wr = open('..//Input-Output//output.txt', 'w')
d = []
for a in f:
    c = a.strip()
    d.append(c)

meal_cost   = float(d[0])
tip_percent = int  (d[1])
tax_percent = int  (d[2])
#---Compute
def meal_compute(meal,tip,tax):
    tip        = meal * (tip/100)
    tax        = meal * (tax/100)
    total_cost = meal + tax + tip
    return int(total_cost)
#---Print Output
round_cost = meal_compute(meal_cost,tip_percent,tax_percent)
wr.write(str(round_cost))
wr.close()