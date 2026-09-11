# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().strip().split()))
    c=0
    for i in l:
        if(i==1):
            c+=1
        elif(i==-1):
            c-=1
    
    if(c%2==0):
        print(abs(c//2))
    elif(n%2==1):
        print(-1)
    elif(n%2==0):
        
        print(0)
        