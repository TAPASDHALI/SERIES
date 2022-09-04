## 2^x + 4^x + 6^x + 8^x... N?
N = int(input("Enter N: "))
X = int(input("Enter X: "))
sum = 0
a = 2
for i in range(1, N + 1):
    sum = sum + a**X
    a += 2
print(f'Sum Of Series: {sum}')
