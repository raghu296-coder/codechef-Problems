# cook your dish here
n,k=map(int,input().split())
arr=list(map(int,input().split()))
if n>2*k:
    total=0
    for i in range(0,n,2):
        total+= arr[i]
    print(total)
else:
    print(0)