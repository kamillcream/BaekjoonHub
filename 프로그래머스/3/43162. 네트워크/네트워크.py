from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            for next_node in range(n):
                if computers[node][next_node] == 1 and not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
        
        
        
    return answer


    
        
        