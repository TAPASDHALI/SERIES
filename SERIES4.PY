## 1 + 3 + 5 + 7 ... N
N = int(input("Enter N: "))
sum = 0
a = 1
for i in range(1, N + 1):
    sum = sum + a
    a += 2
print(f'Sum Of Series: {sum}') 