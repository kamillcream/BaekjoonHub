s = str(input())

def is_divided_by_thirty(list_s):
    int_s = int(''.join(map(str, list_s)))
    return int_s % 30 == 0

def solution(s):
    list_s = list(map(int, s))
    list_s.sort(reverse = True)
    
    if not is_divided_by_thirty(list_s):
        return -1


    return int(''.join(map(str, list_s)))

print(solution(s))