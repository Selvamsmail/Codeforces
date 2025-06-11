t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # Step 1: find max value and its position
    max_val = -float('inf')
    for i in range(n):
        for j in range(m):
            if grid[i][j] > max_val:
                max_val = grid[i][j]
                max_pos = (i, j)

    r, c = max_pos
    min_area = n * m 
    
    height = max(r + 1, n - r)
    width = max(c + 1, m - c)
    print(height * width)

