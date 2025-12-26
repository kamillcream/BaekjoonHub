class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        int size = board[0].length;
        
        int[][] danger = new int[size][size];
        int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = {-1,  0,  1,-1, 1,-1, 0, 1};
        
        for(int i = 0; i < size; i++) {
            for(int j = 0; j < size; j++) {
                if(board[i][j] == 1) {
                    danger[i][j] = 1;
                    for(int k = 0; k < 8; k++) {
                        int ni = i + dx[k];
                        int nj = j + dy[k];
                        if (ni >= 0 && ni < size && nj >= 0 && nj < size) {
                            danger[ni][nj] = 1;   
                        }
                    }
                }
            }
        }
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (danger[i][j] == 0) {
                    answer++;
                }
            }
        }

        return answer;
    }
}