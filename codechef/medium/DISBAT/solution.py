import sys

class DSU:
    # Implement the class

if __name__ == "__main__":
    t = int(input())
    
    # Increase the recursion limit (not recommended in general)
    sys.setrecursionlimit(10**6)

    for _ in range(t):
        n = int(input())
        dsu = DSU(n)

        s = [0] + list(map(int, input().split()))

        q = int(input())
        for _ in range(q):
            query = list(map(int, input().split()))
            # Write the code
