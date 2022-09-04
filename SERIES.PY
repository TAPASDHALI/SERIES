## 1 + 2 + 3 + 4 ...N
sum = 0
a = 1
N = int(input("Enter N: "))
for i in range(1, N+1):
    sum = sum + a
    a += 1
print(f'Sum of Series: {sum}')