def solution(babbling):
    can_words = ["aya", "ye", "woo", "ma"]
    count = 0

    for i in babbling:
        for j in can_words:
            i = i.replace(j, ' ')
        if i.strip() == '':
            count += 1

    return count