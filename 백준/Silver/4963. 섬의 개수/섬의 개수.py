from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, grid, h, w):
    # 상하좌우 및 대각선 방향 설정
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    # 큐를 이용한 BFS
    queue = deque([(x, y)])
    grid[x][y] = 0  # 현재 위치 방문 처리
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == 1:
                grid[nx][ny] = 0  # 재방문 방지
                queue.append((nx, ny))

def count_islands(grid, h, w):
    island_count = 0

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                bfs(i,j, grid, h, w)
                island_count += 1

    return island_count

def main():
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        grid = []
        for i in range(h):
            grid.append(list(map(int, input().split())))

        result = count_islands(grid, h, w)
        print(result)

if __name__ == "__main__":
    main()
