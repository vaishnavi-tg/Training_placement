string=input()
vc=0
cc=0
v="aeiou"
c="bcdfghjklmnpqrstvwxyz"
for i in string:
    if i in v:
        vc+=1
    else:
        cc+=1

print("Vowels count",vc)
print("consonant count",cc)            