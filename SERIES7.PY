## 9!/X + 13!/X + 17!/X .... N?
import math as m
N = int(input("Enter N: "))
X = int(input("Enter X: "))
sum = 0
a = 9
for i in range(1, N + 1):
    sum = sum + m.factorial(a)/X
    a += 4
print(f'Sum Of Series: {sum}')