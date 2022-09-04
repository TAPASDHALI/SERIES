## 1^3/X + 3^3/X + 5^3/X + 7^3/X.....N?
N = int(input("Enter N: "))
X = int(input("Enter X: "))
sum = 0
a = 1
for i in range(1, N + 1):
    sum = sum + a**3/X
    a += 2
print(f'Sum Of Series: {sum}')