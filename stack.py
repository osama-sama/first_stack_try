# a first try at implementing a stack 
class stack:
    def __init__(self):
        # max is the limit of how much we want to store in our stack
        self.max = 4
        # top is the first element that was added to our stack
        self.top = -1
        # my_stack is the storage to our data 
        self.my_stack = [None]*self.max

    # push adds one element to the top of the stack ,but will give a warning if the stack is already full    
    def push(self,new_data):
        if (self.top) >= (self.max)-1 :
            raise SyntaxWarning('Stack is full')
        else :
            self.top+=1
            self.my_stack[self.top] = new_data

    # pop remove the first element from the stack ,but will give a warning if the stack is already empty    
    def pop(self):
        if self.top<=-1 :
            raise SyntaxWarning('Stack is empty')
        else:
            self.top -=1
            return self.my_stack[self.top]
    # prints the stack 
    def print_stack(self):
        print(self.my_stack[:self.top:-1])
    # return True if the stack is full and will return False elsewise
    def is_full(self):
        return self.top == self.max-1
    # return True if the stack is empty and will return False elsewise
    def is_empty(self) :
        return self.top == -1

