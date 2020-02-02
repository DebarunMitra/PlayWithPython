# import math

# print("hello world")

# print(5+8)

# print(math.gcd(3,6))

# operators
# num1 = 7
# num2 = 3
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1//2) #floor division operator
# print(num1%num2) #modulo operator
# print(num1**2) #Exponentiation
# print(num1^num2) #XOR operator 


# type casting
# num = 1990
# str_num=str(num)
# print(type(num))
# float_num=float(num)
# print(type(float_num))
# print(float_num)
# print(type(str_num))
# print(str_num)


# multiline string
# quote='''Ram,
#     You are awesome'''
# print(quote)

# pattern='''
#         *
#        * *
#       * * *
#         8
# '''
# print(pattern)

# string operation

# harry = "Harry Potter"
# db = "DragonBall Z"
# print(harry[5:11]); #potter
# print(harry.strip()) #cut the spaces before string
# print(len(harry)) #length of string
# print(harry.lower())
# print(harry.upper())
# print(harry.replace("r", "R"))
# print(harry.split(' '))
# sentence = "I like to watch first {1} then {0}".format(db,harry) #old process python version < 3.6
# sentence = f"I like to watch first {db} then {harry}"
# print(sentence)

'''
Python Collection
1. List
2. Tuple
3. Set
4. Dictionary
'''
# List
# py_list=[98,2,100,5,1,4,6,3]
# print(type(py_list))
# print(py_list)
# print(py_list[4])
# print(py_list[2:6])
# py_list[6] = 60  # it changes the original list
# print(py_list)
# print(len(py_list))
# py_list.append(20) #add item at the end
# py_list.insert(1,200) #add item at 1th index 
# py_list.remove(2)  # rempve item from the list 
# py_list.pop() # remove from end
# py_list.pop(4)  # remove from index 4
# del py_list[2] # delete 2th index element
# print(py_list)


#Tuple
#** we can't change the values of tuple 
#** But using type casting we can change the values
# py_tuple=("Tom", "Duke", "Harry")
# print(type(py_tuple))
# tuple_list=list(py_tuple)
# print(py_tuple)
# print(tuple_list)
# tuple_list[1]="John"
# print(tuple_list)
# py_tuple=tuple(tuple_list)
# print(py_tuple)

#Set
# py_set={23, 3,10,40,11,10,60,5,2,1,2,3,4,100, 4, 23}
# print(type(py_set))
# print(len(py_set))
# print(py_set)

#Dictionary
# py_Dict={
#     "Name": "Jack",
#     "CLass": "4",
#     "Marks": 80,
#     "RollNo": 5
# }

# print(type(py_Dict))
# print(py_Dict)
# print(len(py_Dict))


# conditional operator

# age= input("Enter your age: ")
# age=18
# print(age)

# if(age>18):
#     print("I am above 18")
# elif (age==18):
#     print("I am 18")
# else:
#     print("I am below 18")

#Loop
# for i in range(0,1000):
#     print(i)

# li=[1, 22, "list"]
# for item in li:
#     print(item)

# i=0
# while(i<100):
#     i=i+1
#     if i==78:
#         break  #continue
#     print(i+1)

# Functions
# def myFunction():
#     print("Good Afternoon Buddy")
#     print("Hi, Buddy")
#     print("How are You")

# myFunction()

# def sum(a,b):
#     print("Inside sum function")
#     return a+b

# print(sum(4,8))

# Class

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary


# harry = Employee("Harry","500")

# print(type(harry))
# print(harry.name)
# print(harry.salary )