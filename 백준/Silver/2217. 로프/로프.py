def max_weight_lifted(n, ropes):
    ropes.sort(reverse = True)
    max_weight = 0
    for i in range(n):
        max_weight = max(max_weight, ropes[i] * (i+1))
    return max_weight

n = int(input())
ropes = [int(input()) for _ in range(n)]
print(max_weight_lifted(n, ropes))