x=[100,110,120,130,140,150]
list=[]
for number in x:
    mum=number*5
    list.append(mum)
print(list)



def divisible_by_three(n):
    numbers=range(1,n+1)
    for number in numbers:
        if(number%3==0):
            print(number)
divisible_by_three(20)


x=[[1,2],[3,4],[5,6]]
def flat_list(nested):
    flat_list=[]
    for sublist in nested:
        for num in sublist:
            flat_list.append(num)
    print(flat_list)
flat_list(x)



def smallest(unsorted_numbers):
   
    return min(unsorted_numbers)
print(smallest([3,6,8,2,4,1,5,7]))



def remove_duplicate():
    list_x=['a','b','a','d','b','c','e','f','g','h']
    change_to_set=set(list_x)
    return change_to_set
    
print(remove_duplicate())

def divisible_by_seven():
    list_div_by_7=[]
    for number in range(100,200):
        if number%7==0:
            list_div_by_7.append(number)
    print(list_div_by_7)
divisible_by_seven()






students=[
    {"age":19,"name":"Eunice"},
    {"age":18,"name":"Agnes"},
    {"age":19,"name":"Teresa"},
    {"age":19,"name":"Asha"}

]
def greetings(students):
    for student in students:
        name=student["name"]
        age=student["age"]
        print(f"Hello {name} your born in {2021-age}")
greetings(students)


import math
class Rectangle():
    def __init__(self,length,width):

        self.length= length
        self.width= width
    def permiter(self):
        return self.length +self.length+self.width
    def area(self):
        return self.length*self.width

rectangle=Rectangle(10,12)
print(rectangle.permiter())
print(rectangle.area())  