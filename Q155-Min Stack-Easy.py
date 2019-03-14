'''
Question: 
  155. Min Stack

Descrition: 
  Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
  push(x) -- Push element x onto stack.
  pop() -- Removes the element on top of the stack.
  top() -- Get the top element.
  getMin() -- Retrieve the minimum element in the stack.

Examples:

  MinStack minStack = new MinStack();
  minStack.push(-2);
  minStack.push(0);
  minStack.push(-3);
  minStack.getMin();   --> Returns -3.
  minStack.pop();
  minStack.top();      --> Returns 0.
  minStack.getMin();   --> Returns -2.
'''

#Python3 Code:

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        #Solution
        #解题思路：开辟两个栈，一个栈是普通的栈，一个栈用来维护最小值的队列。
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        self.stack1.append(x)
        if len(self.stack2) == 0 or x <= self.stack2[-1]:
            self.stack2.append(x)

    def pop(self) -> None:
        v = self.stack1[-1]
        self.stack1.pop()
        if v == self.stack2[-1]:
            self.stack2.pop()
        
    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()