cps = int(input('cps: '))

result = 2/cps 
if cps > 70:
    result = 1.45/cps

result = float('{:.3f}'.format(result))
print(result)

# 0.0035

# 0.05 ~ 30 cps
# 0.075 ~ 25 cps
# 0.1 ~ 20 cps
# 0.5 ~ 4 cps
# 1 = 2 cps