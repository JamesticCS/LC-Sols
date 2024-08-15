class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack or val < self.minstack[-1]:
                self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minstack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()