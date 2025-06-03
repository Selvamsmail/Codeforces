# Write your solution here
# 3
# a
# bbbb
# az

n = int(input())
for _ in range(n):
    st = input()
    flag = 0 
    ans = []
    for ch in st:
        strngs = [j for j in map(chr,range(97,123)) if j!=ch]
        if flag == 0:
            ans.append(min(strngs))
        else:
            ans.append(max(strngs))
        flag ^= 1
    print(''.join(ans))