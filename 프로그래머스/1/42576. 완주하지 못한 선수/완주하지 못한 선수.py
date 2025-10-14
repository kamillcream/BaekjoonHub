from collections import Counter

def solution(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    
    diff = p_counter - c_counter
    
    return list(diff.keys())[0]