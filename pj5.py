#to print cube root and square root of numbers from 1 to 10
import math
width = 10
precision = 4
for n in range(1,10):
    s= math.sqrt(n)
    c = math.pow(n,1/3)
    print(f'{n:^5}{s:{width}.{precision}}{c:{width}.{precision}}')
