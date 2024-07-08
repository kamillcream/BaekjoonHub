import sys
input = sys.stdin.readline

def dfs(V, E, R):
    visited = [False] * (V + 1)
    depths = [-1] * (V + 1)
    
    stack = [(R, 0)]  # 시작 노드와 깊이를 스택에 저장
    
    while stack:
        node, curr_depth = stack.pop()
        if not visited[node]:
            visited[node] = True
            depths[node] = curr_depth
            for neighbor in sorted(E[node], reverse=True):  # 내림차순으로 스택에 넣어야 오름차순으로 처리됨
                if not visited[neighbor]:
                    stack.append((neighbor, curr_depth + 1))
    
    return depths[1:]  # 1부터 N까지의 깊이를 반환

def main():
    N, M, R = map(int, input().split())
    E = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v = map(int, input().split())
        E[u].append(v)
        E[v].append(u)
      
    result = dfs(N, E, R)
    
    for d in result:
        print(d)

if __name__ == "__main__":
    main()
