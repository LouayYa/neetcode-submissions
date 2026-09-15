class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()

        for ch in s:
            if (ch == '(' or ch == '{' or ch == '['):
                stack.append(ch)
            
            elif ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif ch == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif ch == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
        