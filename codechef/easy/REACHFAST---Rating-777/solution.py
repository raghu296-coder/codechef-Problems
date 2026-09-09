# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    count=0
    for i in range(n):
        arr[i]=arr[i]+k
        if(arr[i]%7==0):
            count+=1
    print(count)
        