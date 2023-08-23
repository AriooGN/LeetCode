class MinStack:
    def __init__(self):
        self.top_idx = -1  # Initialize top index as -1
        self.stack = []    # Initialize the stack as an empty list

    def push(self, val: int) -> None:
        self.stack.append(val)  # Append the value to the stack
        self.top_idx += 1       # Increment the top index

    def pop(self) -> None:
        if self.top_idx >= 0:
            self.stack.pop()    # Remove the last element from the stack
            self.top_idx -= 1   # Decrement the top index

    def top(self) -> int:
        if self.top_idx >= 0:
            return self.stack[self.top_idx]  # Return the top element
        else:
            return None

    def getMin(self) -> int:
        if self.top_idx >= 0:
            return min(self.stack)  # Find the minimum element in the stack
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
