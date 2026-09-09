# REACHFAST - Rating 777

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-09T16:43:54.955Z  

```py
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
        
```

---

[View on CodeChef](https://www.codechef.com/problems/REACHFAST)