class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = ''.join(char.lower() for char in str(x))
        return str(x) == new_x[::-1]

    def isPalindrome2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
