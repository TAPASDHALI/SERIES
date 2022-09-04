## 10 + 9 + 8 + 7.....N
N = int(input("Enter N: "))
sum = 0
a = 10
for i in range(1, N + 1):
    sum = sum + a
    a -= 1
print(f'Sum Of Series: {sum}')