def function1():
    print("hello")

function1()

def name(firstname,surname):
    print(firstname,surname)


name("narasimha","balagolla")
name(surname="balagolla",firstname="narasimha")

#default argumants

def add(x,y=9):
    print(x+y)

add(5)

#we cannot create a function with default arguments first and requred next

# def func(x=10,y):
#     pass

# func(5)


def add1(a,b):
    return a+b

res1=add1(4,3)
print(res1)