N, S = map(int, input().split())
nums = list(map(int, input().split()))
res = 0

def dfs(curr_sum, index):
    global res
    if index == N:  # 모든 숫자를 탐색한 경우
        return

    # 현재 숫자를 포함하는 경우
    if curr_sum + nums[index] == S:  # 합이 S가 되는 경우
        res += 1
    dfs(curr_sum + nums[index], index + 1)  # 현재 숫자를 포함

    # 현재 숫자를 포함하지 않는 경우
    dfs(curr_sum, index + 1)

dfs(0, 0)
print(res)
