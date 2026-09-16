# cook your dish here
for _ in range(int(input())):
    N, K = map(int, input().split())

    if N - K == 1:
        print("No")
    else:
        print("Yes")