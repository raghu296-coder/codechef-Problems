# MINFLIPS - Rating 778

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-11T08:42:24.980Z  

```py
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    free=min(x,y,z)
    re=-free+(x+y+z)
    print(re)
```

---

[View on CodeChef](https://www.codechef.com/problems/MINFLIPS)