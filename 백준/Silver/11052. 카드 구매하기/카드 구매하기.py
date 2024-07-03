import sys

input = sys.stdin.readline

def sol(N, P):
    dp = [0] * (N + 1)
    
    for i in range(1, N+1):
        max_price = 0
        for j in range(1, i+1):
            if j <= len(P):
                max_price = max(max_price, dp[i-j] + P[j-1])
        dp[i] = max_price

    return dp[N]

N = int(input())
P = list(map(int, input().split()))

res = sol(N, P)
print(res)