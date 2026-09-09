# cook your dish here
for _ in range(int(input())):
    x,y,r= map(int,input().split())
    target =(r//30) + x
    if(target % y==0):
        print(target//y)
    else:
        print((target//y)+1)
    
    