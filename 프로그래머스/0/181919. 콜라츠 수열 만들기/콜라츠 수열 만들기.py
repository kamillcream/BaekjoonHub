def solution(n):
    answer = []
    while n != 1:
        answer.append(n)
        if n % 2 == 0:
            n = fun_even(n)
            continue
        if n % 2 == 1:
            n = fun_odd(n)
            continue
            
    answer.append(n)
            
    return answer


def fun_even(n):
    return n // 2

def fun_odd(n):
    return n * 3 + 1