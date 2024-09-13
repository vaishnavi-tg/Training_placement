def reverse(str):
    words=str.split()
    reverse=words[::-1]
    reverse_string=" ".join(reverse)
    print("Reversed string is",reverse) 


r=reverse("Hello world i am gng to be a data scientist")
print(r)





str=input("Enter the string\n")
words=str.split()
reverse=words[::-1]
reverse_string=" ".join(reverse)
print("The reversed string is",reverse_string)