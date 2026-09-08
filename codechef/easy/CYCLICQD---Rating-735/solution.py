# cook your dish here
for _ in range(int(input())):
    a,b,c,d=list(map(int,input().split()))
    if(a+c==180 & d+b==180):
        print("YES")
    else:
        print("NO")