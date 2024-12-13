class Sol:
    def isPalindrome(self, s:str) -> int:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return 0
            
        return 1
    
sol = Sol()
s = input()
print(sol.isPalindrome(s))