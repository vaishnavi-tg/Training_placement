rows=int(input())
number=0
for i in range(0,rows):
    for j in range(0,i+1):
        print(number,end=" ")
        number+=1
    print()    