# cook your dish here
r,o,c =map(int,input().split())
score=20-o
rem=score*6
final=c+rem*6
if(final > r):
    print("YES")
else:
    print("NO")