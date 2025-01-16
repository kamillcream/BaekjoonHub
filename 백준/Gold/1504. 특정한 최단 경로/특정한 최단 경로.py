from collections import defaultdict
import heapq

# 다익스트라 알고리즘 정의
def dijkstra(start, graph, n):
    dist = defaultdict(lambda: float('inf'))  # 무한대로 초기화
    Q = [(0, start)]
    dist[start] = 0

    while Q:
        time, node = heapq.heappop(Q)
        # 이미 처리된 노드면 무시
        if time > dist[node]:
            continue
        # 인접 노드 탐색
        for v, w in graph[node]:
            alt = time + w
            if alt < dist[v]:  # 더 짧은 경로 발견
                dist[v] = alt
                heapq.heappush(Q, (alt, v))

    return dist

# 입력 처리
n, e = map(int, input().split())
routes = []
for i in range(e):
    routes.append(list(map(int, input().split())))

v1, v2 = map(int, input().split())

# 그래프 생성
graph = defaultdict(list)
for u, v, w in routes:
    graph[u].append((v, w))
    graph[v].append((u, w))

# 다익스트라 실행
dist_from_1 = dijkstra(1, graph, n)        # 1번에서 모든 노드까지
dist_from_v1 = dijkstra(v1, graph, n)     # v1에서 모든 노드까지
dist_from_v2 = dijkstra(v2, graph, n)     # v2에서 모든 노드까지

# 경로 계산
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]  # 1 → v1 → v2 → n
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]  # 1 → v2 → v1 → n

# 최소 경로 선택
result = min(path1, path2)

# 도달할 수 없는 경우 처리
if result >= float('inf'):
    print(-1)
else:
    print(result)
