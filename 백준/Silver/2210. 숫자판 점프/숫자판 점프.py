board = [list(input().split()) for _ in range(5)]
res = []
    
    
def dfs(cur_path, i, j):
    if len(cur_path) == 6:
        if cur_path not in res:
            res.append(cur_path)
        return
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(cur_path + board[nx][ny], nx, ny)
            
for i in range(5):
    for j in range(5):
        dfs("", i, j)
        
        
print(len(res))