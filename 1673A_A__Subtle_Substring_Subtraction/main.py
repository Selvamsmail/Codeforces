# Write your solution here
# 5
# aba
# abc
# cba
# n
# codeforces

n = int(input())
letters = {v:k+1 for k,v in enumerate(list(map(chr, range(97,123))))}
for _ in range(n):
    st = list(input())
    even_or_odd = ('even' if len(st) % 2 == 0 else 'odd')
    
    for i in range(len(st)):
        st[i] = letters[st[i]]
        
    if even_or_odd == 'even':
        print(f'Alice {sum(st)}')
    else:
        bob = min(st[0],st[-1])
        alice = sum(st)-bob
        print(f'Alice {alice - bob}' if alice > bob else f'Bob {bob-alice}')
        

################################################### Alternate Solution.################################

# n = int(input())       
# for _ in range(n):
#     s = input()
#     values = [ord(c) - ord('a') + 1 for c in s]
    
#     if len(values) % 2 == 0:
#         print(f"Alice {sum(values)}")
#     else:
#         bob = min(values[0], values[-1])
#         alice = sum(values) - bob
#         if alice > bob:
#             print(f"Alice {alice - bob}")
#         else:
#             print(f"Bob {bob - alice}")