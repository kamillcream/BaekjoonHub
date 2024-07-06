import sys
input = sys.stdin.readline

def main():
    T = int(input().strip())
    
    for _ in range(T):
        N = int(input().strip())
        candidates = []
        
        for i in range(N):
            docs, interview = map(int, input().strip().split())
            candidates.append((docs, interview))
        
       
        candidates.sort()
        
      
        cnt = 1
        min_interview = candidates[0][1]
        
        for i in range(1, N):
            if candidates[i][1] < min_interview:
                
                cnt += 1
                min_interview = candidates[i][1]  
        
        print(cnt)

if __name__ == "__main__":
    main()
