# 5
# 01111001
# 0000
# 111111
# 101010101
# 011011110111

n = int(input())
for i in range(n):
    st = input()
    scores = []
    count = 0
    for ch in st+'0':
        if ch == '1':
            count += 1
        elif ch == '0':
            if count > 0:
                scores.append(count)
                count = 0
    scores = sorted(scores,reverse=True)
    alice = sum([scores[i] for i in range(0,len(scores),2)])
    print(alice)