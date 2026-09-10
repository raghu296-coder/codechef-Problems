# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    s=min(x,y)
    e=max(x,y)
    if(s==e):
        print(0)
    elif s<e:
        d=e-s
        if d%z==0:
            print(d//z)
        else:
            print((d//z)+1)
        
        
        
