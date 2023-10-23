class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(char for char in s if char.isalnum()).lower()

        for i in range(len(new_s)):
            if new_s[i] != new_s[len(new_s)-1-i]:
                return False
        
        return True
    
    def isPalindrome_2(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())

        return s == s[::-1]
    
    def isPalindrome_3(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and s[l].isalnum() == False:
                l += 1
            while r > l and s[r].isalnum() == False:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        
        return True