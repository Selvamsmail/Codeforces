# Write your solution here
# 2
# 4
# 2 4 2 1
# 1
# 1


n = int(input())
for _ in range(n):
    int(input())
    l = list(map(int,input().split()))
    score = sum(i-1 for i in l)
    print('errorgorn' if score % 2 != 0 else 'maomao90')