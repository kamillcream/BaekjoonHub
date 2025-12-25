class Solution {
    public int solution(int n) {
        int answer = 0;
        if (n % 2 == 0) {
            answer = evenCalculate(n);
        } else {
            answer = oddCalculate(n);
        }
        return answer;
    }
    
    public int oddCalculate(int n) {
        int res = 0;
        for(int i = 1; i <= n; i += 2) {
            res += i;
        }
        return res;
    }
    
    public int evenCalculate(int n) {
        int res = 0;
        for(int i = 2; i <= n; i += 2) {
            res += Math.pow(i, 2);
        }
        return res;
    }
}