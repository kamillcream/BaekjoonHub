def dfs(path, index):
    if len(path) == 6:
        res.append(path[:])
        return
    for i in range(index, len(nums)):  # index 이후만 탐색
        if i > index and nums[i] == nums[i-1]:
            continue
        dfs(path + [nums[i]], i + 1)  # i + 1로 다음 요소 탐색


while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0 and len(nums) == 1:  # 종료 조건
        break
    res = []
    nums.pop(0)
    nums.sort()
    dfs([], 0)
    for i in res:
        print(*i)  # 리스트 요소를 공백으로 구분하여 출력
    print()
