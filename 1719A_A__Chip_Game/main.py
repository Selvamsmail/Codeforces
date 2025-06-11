t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if (n + m) % 2 == 0:
        print("Tonya")
    else:
        print("Burenka")