from collections import Counter

def solution(nums):
    nums_counter = Counter(nums)
    
    return min(len(nums) / 2, len(nums_counter))
    