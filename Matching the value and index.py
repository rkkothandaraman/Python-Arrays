N=int(input())
A=[int(x) for x in input().split()[:N]]
li=[]
for i in range(N):
    if(i==A[i]):
        li.append(i)
if(len(li)==0):
    print('-1')
else:
    for j in range(len(li)):
        print(li[j], end=" ")
        
