# cook your dish here
x,y=map(int,input().split())
z=x+y
if z%2==0:
    give=x-((x+y)//2)
    print(give)
else:
    print(-1)