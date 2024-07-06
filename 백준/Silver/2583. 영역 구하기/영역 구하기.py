import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, grid, visited, M, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])
    grid[x][y] = 1  
    visited[x][y] = True
    area = 1
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                grid[nx][ny] = 1
                queue.append((nx, ny))
                area += 1
    
    return area

def count_areas(grid, M, N):
    visited = [[False] * N for _ in range(M)]
    area_cnt = []
    
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0 and not visited[i][j]:  
                area_size = bfs(i, j, grid, visited, M, N)
                area_cnt.append(area_size)
    
    return area_cnt

def main():
    M, N, K = map(int, input().split())
    
    grid = [[0] * N for _ in range(M)]
    
    for _ in range(K):
        y1, x1, y2, x2 = map(int, input().split())
        for x in range(x1, x2):
            for y in range(y1, y2):
                if 0 <= x < M and 0 <= y < N:
                    grid[x][y] = 1
    
    areas = count_areas(grid, M, N)
    areas.sort()
    
    print(len(areas))
    print(" ".join(map(str, areas)))

if __name__ == "__main__":
    main()
