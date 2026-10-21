class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        stack = []
        for s in operations:
            match s:
                case '+': 
                    score = stack[-1] + stack[-2]
                    stack.append(score)
                case 'D':
                    score = 2 * stack[-1]
                    stack.append(score)
                case 'C':
                    stack.pop()
                case _:
                    stack.append(int(s))
        
        return sum(stack)

        