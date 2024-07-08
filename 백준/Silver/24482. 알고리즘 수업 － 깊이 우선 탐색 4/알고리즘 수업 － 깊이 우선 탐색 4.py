import sys
input = sys.stdin.readline

def dfs(V, E, R):
    visited = [False] * (V+1)
    depths= [-1] * (V+1)
    
    stack = [(R, 0)]
    
    while stack:
        node, depth = stack.pop()
        if not visited[node]:
            visited[node] = True
            depths[node] = depth
            for n in sorted(E[node]):
                if not visited[n]:
                    stack.append((n, depth+1))
                    
    return depths[1:]  
    
    
def main():
    N, M, R = map(int, input().split())
    E = [[] for _ in range(N+1)]
    
    for _ in range(M):
        u, v = map(int, input().split())
        E[u].append(v)
        E[v].append(u)
        
    result = dfs(N, E, R)
    
    for d in result:
        print(d)
        
if __name__ == "__main__":
    main()