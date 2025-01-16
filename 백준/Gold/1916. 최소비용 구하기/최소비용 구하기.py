from collections import defaultdict
import heapq

n = int(input())
m = int(input())
cities = []

for i in range(m):
    cities.append(list(map(int, input().split())))
    
start, end = map(int, input().split())

graph = defaultdict(list)

for u, v, w in cities:
    graph[u].append((v, w))

Q = [(0, start)]

dist = defaultdict(int)

while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heapq.heappush(Q, (alt, v))
            
print(dist.get(end))