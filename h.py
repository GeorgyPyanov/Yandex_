g = int(input())
a = 1
b = 3
k = False
for i in range(g - 1):
    if k:
        a += 1 / b
    else:
        a -= 1 / b
    b += 2
    k = not k
print(round(a * 4, 6))