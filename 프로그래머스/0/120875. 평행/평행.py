from itertools import combinations

def solution(dots):
    for i in range(4):
        for j in range(i + 1, 4):
            # 두 점을 골라 첫 번째 선
            rest = [k for k in range(4) if k not in [i, j]]
            x1, y1 = dots[i]
            x2, y2 = dots[j]
            x3, y3 = dots[rest[0]]
            x4, y4 = dots[rest[1]]

            # 교차곱으로 기울기 비교
            if (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1):
                return 1
    return 0