def solution(lines):
    # 좌표 범위는 -100 ~ 100
    arr = [0] * 201   # index 0 → -100, index 200 → 100

    # 각 선분마다 구간 표시
    for start, end in lines:
        # 선분은 start <= x < end (끝은 포함하지 않음)
        for x in range(start, end):
            arr[x + 100] += 1  # -100 보정

    # 2개 이상 겹친 구간의 길이
    answer = sum(1 for x in arr if x >= 2)
    return answer