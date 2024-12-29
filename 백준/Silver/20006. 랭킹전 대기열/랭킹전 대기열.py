n, m = map(int, input().split())
people = []

# 입력 처리
for _ in range(n):
    l, n = input().split()
    people.append((int(l), n))

rooms = []  # 방 목록

def room_allocate(player, rooms, m):
    for room_level, players in rooms:
        # 방의 기준 레벨과 정원 확인
        if room_level - 10 <= player[0] <= room_level + 10 and len(players) < m:
            players.append(player)
            return
    # 입장 가능한 방이 없으면 새 방 생성
    rooms.append((player[0], [player]))

# 플레이어를 방에 배정
for player in people:
    room_allocate(player, rooms, m)

# 출력
for room_level, players in rooms:
    if len(players) == m:
        print("Started!")
    else:
        print("Waiting!")
    # 닉네임 기준 정렬 후 출력
    players.sort(key=lambda x: x[1])
    for player in players:
        print(player[0], player[1])
