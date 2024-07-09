import sys
input = sys.stdin.readline

def findRank(t, n, total_scores, entry_counts, last_submit_times):
    my_team_score = total_scores[t]
    my_team_entry = entry_counts[t]
    my_team_time = last_submit_times[t]
    
    rank = 1  # 자신의 초기 등수는 1위로 설정
    
    for team_id in range(1, n+1):
        if team_id == t:
            continue  # 자신의 팀은 건너뜀
        
        other_team_score = total_scores[team_id]
        other_team_entry = entry_counts[team_id]
        other_team_time = last_submit_times[team_id]
        
        if other_team_score > my_team_score:
            rank += 1
        elif other_team_score == my_team_score:
            if other_team_entry < my_team_entry:
                rank += 1
            elif other_team_entry == my_team_entry:
                if other_team_time < my_team_time:
                    rank += 1
    
    return rank

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n, k, t, m = map(int, input().split())
        team_scores = [[0] * (k+1) for _ in range(n+1)]
        total_scores = [0] * (n+1)
        entry_counts = [0] * (n+1)
        last_submit_times = [0] * (n+1)
        
        for time_index in range(1, m+1):
            tid, pno, gscore = map(int, input().split())
            entry_counts[tid] += 1
            last_submit_times[tid] = time_index
            if team_scores[tid][pno] < gscore:
                total_scores[tid] += gscore - team_scores[tid][pno]
                team_scores[tid][pno] = gscore
        
        results.append(findRank(t, n, total_scores, entry_counts, last_submit_times))
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
