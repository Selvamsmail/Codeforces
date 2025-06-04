# 3
# 12
# 132
# 487456398
n = int(input())
for _ in range(n):
    l = list(input())
    if len(l) == 2 and l[1] > l[0]:
        print(l[1])
    else:
        print(min(l))