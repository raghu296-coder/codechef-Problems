for _ in range(int(input())):
    x,y,z=map(int,input().split())
    free=min(x,y,z)
    re=-free+(x+y+z)
    print(re)