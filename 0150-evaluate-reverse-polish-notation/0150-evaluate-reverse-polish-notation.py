class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Create an empty stack to store operands and results
        
        for char in tokens:
            if char in "+-*/" and len(stack) >= 2:
                # If the current element is an operator and there are at least two operands in the stack
                num1 = int(stack.pop())  # Pop the top operand from the stack
                num2 = int(stack.pop())  # Pop the second operand from the stack
                
                # Perform the operation based on the operator
                if char == "+":
                    stack.append(num2 + num1)  # Push the result of addition onto the stack
                elif char == "-":
                    stack.append(num2 - num1)  # Push the result of subtraction onto the stack
                elif char == "/":
                    stack.append(int(num2 / num1))  # Push the result of division onto the stack
                elif char == "*":
                    stack.append(num2 * num1)  # Push the result of multiplication onto the stack
            else:
                stack.append(char)  # If the element is not an operator, push it onto the stack as an operand
        
        return int(stack.pop())  # The final result will be at the top of the stack
