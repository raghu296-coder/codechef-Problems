# cook your dish here
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    c= n//2
    d=n-c
    res=c*a+d*b
    print(res)
