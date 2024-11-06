# Array and simple queries


# Enter your code here. Read input from STDIN. Print output to STDOUT

from array import array

def array_queries(arr: array[int], queries: list[list[int]]) -> None:
    for t, i, j in queries:
        if t == 1:
            arr = arr[i-1:j] + arr[:i-1] + arr[j:]
        else:
            arr = arr[:i-1] + arr[j:] + arr[i-1:j]
    
    print(abs(arr[0] - arr[-1]))
    print(*arr)


if __name__ == '__main__':
    first = list(map(int, input().split()))
    N, M = first[0], first[1]
    arr = array('i', [int(val) for val in input().split()])
    queries = [list(map(int, input().split())) for _ in range(M)]
    array_queries(arr, queries)
