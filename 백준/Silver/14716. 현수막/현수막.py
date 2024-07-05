from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, grid, M, N):
    directions = [(-1,0), (1,0), (0,-1), (0,1), (-1, -1), (-1,1), (1, -1), (1,1)]
    queue = deque([(x,y)])
    grid[x][y] = 0
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<M and 0<=ny<N and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                queue.append((nx, ny))
                

def count_word(grid, M, N):
    word_count = 0
    
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                bfs(i, j, grid, M, N)
                word_count += 1
                
    return word_count


def main():
    M, N = map(int, input().split())
    grid = []
    for i in range(M):
        grid.append(list(map(int, input().split())))
        
    result = count_word(grid, M, N)
    print(result)
    
if __name__ == "__main__":
    main()