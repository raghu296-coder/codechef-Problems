# cook your dish here

for _ in range(int(input())):
    n,m=map(int,input().split())
    a=n*m
    if a%2==0:
        print("Yes")
    else:
        print("NO")