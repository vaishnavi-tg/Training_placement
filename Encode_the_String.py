def encode_string(input_string):
    res=''
    for char in input_string:
        sq_dig=str(int(char)**2)
        res+=sq_dig
    return res

a=encode_string("578")
print(a)    


