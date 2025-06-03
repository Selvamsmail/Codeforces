# 2
# 2 1 1
# 2
# 1
# 5 2 3
# 2 3
# 1 4 5

t = int(input())
for _ in range(t):
    n, k1, k2 = map(int, input().split())
    p1_cards = list(map(int, input().split()))
    p2_cards = list(map(int, input().split()))

    if max(p1_cards) > max(p2_cards):
        print("YES")
    else:
        print("NO")