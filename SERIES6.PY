## X^1+ X^2 + X^3 + X^4 ... N
N = int(input("Enter N: "))
X = int(input("Enter X: "))
sum = 0
a = 1
for i in range(1, N + 1):
    sum = sum + X**a
    a += 1
print(f'Sum Of Series: {sum}')
