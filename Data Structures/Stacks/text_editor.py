# Simple Text Editor


# Enter your code here. Read input from STDIN. Print output to STDOUT
def text_editor(ops):
    text = ""
    stack = []
    
    for op_str in ops:
        op = op_str.split()
        
        if op[0] == '1':
            text += op[1]
            stack.append((1, op[1]))
        elif op[0] == '2':
            pop = text[-int(op[1]):]
            text = text[:-int(op[1])]
            stack.append((2, pop))
        elif op[0] == '3':
            print(text[int(op[1]) - 1])
        else:
            code, s = stack.pop()
            if code == 1:
                text = text[:-len(s)]
            else:
                text += s
   
            
if __name__ == '__main__':
    n = int(input())
    ops = []
    
    for _ in range(n):
        ops.append(input())
        
    text_editor(ops)
