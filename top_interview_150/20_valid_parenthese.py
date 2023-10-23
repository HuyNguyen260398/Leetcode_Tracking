class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for char in s:
            if char not in brackets_dict.keys():
                if len(stack) == 0:
                    return False
                elif brackets_dict[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False
        
    def isValid2(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack