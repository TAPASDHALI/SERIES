## 2 + 4 + 6 + 8 ... 20
N = int(input("Enter N: "))
# N = 20
sum = 0
a = 2
for i in range(1, N + 1):
    sum = sum + a
    a += 2
    # print(f'Sum Of Series: {a}')
print(f'Sum Of Series: {sum}')