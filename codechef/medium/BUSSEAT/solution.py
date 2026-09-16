# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    re=k-n
    if n>=k:
        print(0)
    else:
        print(re*2)