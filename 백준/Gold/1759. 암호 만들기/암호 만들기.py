from collections import Counter
L, C = map(int, input().split())
chars = list(map(str, input().split()))
chars.sort()            
res = []
aeiou = {"a", "e", "i", "o", "u"}

def dfs(path, index):
    if len(path) == L:
             count = Counter(path)
             vowels = sum(count[char] for char in aeiou)
             consonants = len(path) - vowels
             if vowels >= 1 and consonants >= 2:
                 res.append(''.join(path))
             return
    for i in range(index, C):
             dfs(path + [chars[i]], i + 1)
dfs([], 0)
for i in res:
     print(i)