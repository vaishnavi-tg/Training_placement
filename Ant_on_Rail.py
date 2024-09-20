n=int(input())
arr=list(map(int,input().split()))
count=0
pos=0
for i in arr:
   pos+=i
   if pos==0:
      count+=1

print(count)



