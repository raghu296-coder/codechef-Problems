# cook your dish here
for _ in range(int(input())):
    x,a,y,b=map(int,input().split())
    alice=x/a
    bob=y/b
    if(alice >bob):
        print("Alice")
    elif (alice==bob):
        print("Equal")
    else:
        print("Bob")