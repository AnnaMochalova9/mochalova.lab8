n = int(input("ввести кол-во строк "))
m = int(input("ввести кол-во столбцов "))
x = []
for i in range(n):
    y = []
    for j in range(m):
        y.append(int(input()))
    x.append(y)
print(x)
