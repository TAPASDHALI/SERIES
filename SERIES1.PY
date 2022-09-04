## 9 + 13 + 17 ... N
N = int(input("Enter N: "))
sum = 0
a = 9
for i in range(1, N+1):
    sum = sum + a
    a += 4
    # print(f'N Numbers: {a}')
print(f'Sum Of Series: {sum}')