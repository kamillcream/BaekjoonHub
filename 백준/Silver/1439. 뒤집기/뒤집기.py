def reverse(original, target):
    prev = original[0]
    if prev == target[0]:
        cnt = 0
    else:
        cnt = 1
    for i in range(1, len(original)):
        if original[i] != target[i]:
            if prev != original[i]:
                cnt += 1
        prev = original[i]
    return cnt

s = str(input())

s0 = '0' * len(s)
s1 = '1' * len(s)

print(min(reverse(s, s0), reverse(s, s1)))