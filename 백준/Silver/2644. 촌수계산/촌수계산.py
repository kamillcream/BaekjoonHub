# 백준 2644번: 촌수계산

import sys
sys.setrecursionlimit(10000)

n = int(input())  # 전체 사람 수
a, b = map(int, input().split())  # 촌수를 계산할 두 사람
m = int(input())  # 관계 수

graph = [[] for _ in range(n + 1)]  # 인접 리스트
visited = [False] * (n + 1)
result = -1  # 촌수 결과값

# 관계 입력 받기
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향 연결

def dfs(v, depth):
    global result
    visited[v] = True
    if v == b:
        result = depth
        return
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)

dfs(a, 0)
print(result)