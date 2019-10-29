def year(a):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print('високосный')
    else:
        print('невисокосный')  
for a in range(2000, 2018, 1):
 year(a)
              