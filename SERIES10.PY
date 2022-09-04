## 2/10 + 4/9 + 6/8 + 8/7...N?
N = int(input("Enter N: "))
D = int(input("Enter D: "))
a = 2
sum = 0
for i in range(1, N + 1):
    sum = sum + a/D
    a += 2
    D -= 1
print(f'Sum Of Series: {sum}')