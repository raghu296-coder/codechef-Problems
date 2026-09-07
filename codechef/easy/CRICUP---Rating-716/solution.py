# cook your dish here
for _ in range(int(input())):
    x,y,D=map(int,input().split())
    
    d=abs(x-y)
    if(d<=D):
        print("YES")
    else:
        print("NO")