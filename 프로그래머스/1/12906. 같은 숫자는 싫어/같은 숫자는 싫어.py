from collections import deque

def solution(arr):
    answer = []
    top = 1000001
    for i in arr:
        if top != i:
            answer.append(i)
            top = i
                
    
    return answer
    