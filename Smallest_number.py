'''8) Smallest Number 
Prince participated in three Olympiads at school and received marks for all of them. 
He is interested in finding out the lowest mark he obtained among the three 
Olympiads. Write a program to find the minimum mark. 
Example: 
Input: 50 66 23 
Output: Smallest number is 23 '''



      

# This is the inbuilt input approach and it is using functions
def get_marks(marks):
    return min(marks)
marks=[12,46,78,45,23,45]
g=get_marks(marks)
print(g)

def get_marks1():
    print("Enter the marks of the olympaid")
    marks=list(map(int,input().split()))
    print("The lowest marks scored is",min(marks))
    
g1=get_marks1()
print(g1)







