right = int(input()) + 1
left = 0
la = (left + right) // 2
print(la)
while True:
    k = int(input())
    if k == 0:
        break
    if k == 1:
        left = la
    if k == -1:
        right = la
    la = (left + right) // 2
    print('{{ la }}')
