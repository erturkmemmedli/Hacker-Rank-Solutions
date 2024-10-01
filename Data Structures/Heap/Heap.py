# QHEAP1


from bisect import insort

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    heap = []
    
    for _ in range(n):
        op = input().split()
        if op[0] == '1':
            insort(heap, int(op[1]))
        elif op[0] == '2':
            heap.remove(int(op[1]))
        else:
            print(heap[0])
