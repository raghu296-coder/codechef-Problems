# cook your dish here
for _ in range(int(input())):
    x=int(input())
    if( x%5!=0):
        print(-1)
    else:
        print((x+5)//10)
