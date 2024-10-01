# Queue using Two Stacks


# Enter your code here. Read input from STDIN. Print output to STDOUT
class QueueByTwoStacks:
    def __init__(self):
        self.stack = []
        self.temp = []
    
    def enqueue(self, num):
        self.stack.append(num)
    
    def dequeue(self):
        if not self.temp:
            while self.stack:
                self.temp.append(self.stack.pop())
            
        return self.temp.pop()
    
    def peek(self):
        print(self.temp[-1] if self.temp else self.stack[0])
    

if __name__ == '__main__':
    queue = QueueByTwoStacks()
    n = int(input())
    queries = []
    
    for _ in range(n):
        queries.append(input())
        
    for query in queries:
        op = query.split()
        if op[0] == '1':
            queue.enqueue(int(op[1]))
        elif op[0] == '2':
            queue.dequeue()
        else:
            queue.peek()
            
