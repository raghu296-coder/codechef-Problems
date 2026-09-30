# cook your dish here
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    occupied =list(map(int,input().split()))
    occupied=set(occupied)
    count=0
    for i in range(1,n+1):
        if i in occupied:
            continue
        print(i, end=" ")
        count+=1
        if count==k:
            break
    print()
    