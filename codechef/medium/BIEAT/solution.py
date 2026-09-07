# cook your dish here
x,y,z=map(int,input().split())
while x!=0:
    if x/(2**z):
        print(x/(2**z))
    else:
        print(0)
