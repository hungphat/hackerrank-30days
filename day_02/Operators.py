f  = open('input.txt', 'r')  #TODO Phat tep input.txt nay dung chung voi bai day_01 ?
wr = open('output.txt', 'w') #em da tach ra moi bai se co in out rieng roi a
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