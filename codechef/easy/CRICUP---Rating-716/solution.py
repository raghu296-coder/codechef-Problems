# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    d=x-y
    if(d<=z):
        print("YES")
    else:
        print("NO")