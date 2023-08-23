class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack:  # Check if the stack is empty before popping
                    return False
                
                # Check for matching opening brackets on the stack
                if char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0  # Check if the stack is empty at the end
