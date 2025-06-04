# 4
# 1
# 6
# 2
# 6 8
# 4
# 1 3 3 7
# 2
# 4 2
# 1
# 50
# 2
# 25 50
# 10
# 1 2 3 4 5 6 7 8 9 10
# 2
# 5 15

n = int(input())
for _ in range(n):
    alic_n = int(input())
    alic_l = list(map(int,input().split()))
    bob_n = int(input())
    bob_l = list(map(int,input().split()))
    
    print("Alice" if max(alic_l) >= max(bob_l) else "Bob")
    print("Alice" if max(alic_l) > max(bob_l) else "Bob")