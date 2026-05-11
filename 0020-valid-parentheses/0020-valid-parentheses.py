class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_to_open_map = {"}" : "{", "]" : "[", ")" : "("}

        for c in s:
            if c  in closing_to_open_map:
                if stack and stack[-1] == closing_to_open_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
