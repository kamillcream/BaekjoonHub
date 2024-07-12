import sys
input = sys.stdin.readline
from collections import deque




def sol(N, R, S):
    frame = deque()  
    recommend = [0] * (R + 1) 

    for student in S:
        recommend[student] += 1

        if student not in frame:
            if len(frame) == N:
            
                min_recommend = min(recommend[std] for std in frame)
                candidates = [std for std in frame if recommend[std] == min_recommend]

                
                for i in range(len(frame)):
                    if frame[i] in candidates:
                        removed_student = frame[i]
                        frame.remove(removed_student)  
                        recommend[removed_student] = 0  
                        break
            
            frame.append(student)

    return list(frame)
            

def main():
    N = int(input())
    R = int(input())
    S = list(map(int, input().split()))
    result = sol(N, R, S)
    result.sort()
    print(*result)
    
if __name__ == "__main__":
    main()