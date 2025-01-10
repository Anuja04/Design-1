"""
Problem: Min Stack
Approach: Use a stack to store the elements. Each element in the stack is a tuple of the element and the minimum element
till that point. The push operation is implemented by checking if the stack is empty. If it is empty, push the element
and the element itself as the minimum element. If not, push the element and the minimum of the current minimum and the
element. The pop operation is implemented by popping the top element. The top operation is implemented by returning the
top element. The getMin operation is implemented by returning the minimum element.
tc: O(1) for all operations
sc: O(n)
"""


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
            return

        current_min = self.stack[-1][1]
        self.stack.append([val, min(current_min, val)])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()