arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
inter=sorted(list(set(arr1)&set(arr2)))
union=sorted(list(set(arr1)|set(arr2)))
print(inter)
print(union)

