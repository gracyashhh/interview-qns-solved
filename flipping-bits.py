p,q=map(int,input().split())
a='{0:08b}'.format(p)
b='{0:08b}'.format(q)
ans=0
for i in range(len(a)):
    if a[i]!=b[i]:
        ans+=1
print(ans)