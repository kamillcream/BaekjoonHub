n, k = map(int, input().split())
usage_order = list(map(int, input().split()))

multitap = []
remove_cnt = 0

for i, device in enumerate(usage_order):
    if device in multitap:
        continue
    if len(multitap) < n:
        multitap.append(device)
        continue

    farthest = -1
    remove_idx = -1
    
    for idx, plugged in enumerate(multitap):
        if plugged not in usage_order[i+1 : ]:
            remove_idx = idx
            break
        else:
             next_use = usage_order[i+1:].index(plugged)
             if next_use > farthest:
                farthest = next_use
                remove_idx = idx
    multitap[remove_idx] = device
    remove_cnt+=1

print(remove_cnt)
