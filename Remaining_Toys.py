'''6) Number of toys 
Akshay has a number of toys and he decided to donate some of them to an NGO. After 
the donation, he still has some toys left. Write a program to help Akshay to determine 
the number of remaining toys. 
Example: 
Input: 50 45 
Output: The remaining number of toys = 5 
Input: 60 6 
Output: The remaining number of toys = 54 '''


htoys=int(input("Enter the number of toys Akshay have with him  "))
dtoys=int(input("Enter the number of toys akshay donated"))
rem=htoys-dtoys
print("The total number of toys remaining with akshay are",rem)



def toys():
    htoys=int(input("Enter the number of toys akshay have    "))
    dtoys=int(input("Enter the number of toys akshay donated "))
    return htoys-dtoys 
t1=toys()
print(t1)