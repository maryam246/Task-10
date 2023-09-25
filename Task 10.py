# Class,Object,Members:
# Example 1.
class computer:
    def config(self): #methods
        print(f"This is i5 machine which have :",'16gb Ram.')

com1 = computer() # object of class
com2 = computer() # also called instance of class
computer.config(com1)
computer.config(com2) # call the config method

com1.config() # Usally this way we used to call class methods
# Example 2.
class Person:
    name = "Ali"
    age = 22
p = Person() # calling the Attributes
print(f'My name is: {p.name} and age is: {p.age}')
# Example 3.
class A():
    school = 'Student'
    def things(self): #"Self" refers to the object which is followed by a class method.
        print('Student must have books,pen,rigister in his bag.')
a = A()
a.things()
print(a.school)
# Example 4.
class number:
    n1 = 'Kiran'
    n2 = 'Muneeb'
    def get_marks(self,x,y):
        print(f'{self.n1} got {x} marks, And {self.n2} get {y}.')
num = number()
num.get_marks(800,890)
# Example 5.
class Details:
    name = 'Areej'
    profession = 'HR'
    def display(self):
        print(f'My name is {self.name} and profession is {self.profession}.')

c= Details()
d = Details()

c.name = 'Fatima'
c.profession = 'Software developer'

d.display()
c.display()

# Data Hiding and Object printing.
#Example 1 Data hiding
class Employee:
    #hiddent data member/privete member in class
    __salary = 50000
e = Employee()
# print(e.__salary) ---> this is not the right way to accessing hidden data
# here we can access the hidden data by tricky syntax
print(e._Employee__salary)
# Example 2:
class num:

    def __init__(self,x):
        self.__x = x
    def __str__(self):
        return '%s' % (self.__x)
n = num(500)
print(n)

# Example 3:
class price:
    __cake = 450
    def __repr__(self):
        return '%s' %(self.__cake)
p = price()
print(p)
# Example 4:
class bus:
    __seats  = 40
    def __init__(self,students):
        self.__students = students
    def __repr__(self):
        return 'Seats in bus is %s and students is %s' % (self.__seats,self.__students)
b = bus(30)
print(b)
#Example 5:
class school:
    __student_name = 'Naeem'
    def __init__(self,age):
        self.age = age
    def __str__(self):
        return '%s:student name and %s:age'%(self.__student_name,self.age)
s = school(32)
print(s)

#Example 2
# String representation/ Printing of class object
# Object printing concept.
class Test:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'My name is : %s and my age is : %s' % (self.x,self.y)

t =Test('kiran',44)
print(t)
#Another method of printing is Example 3
class A:
    def __init__(self,age):
        self.age = age

    def __str__(self):
        return 'The age of ali is %s.' % (self.age)

a =A(22)
print(a)

# Inheritance example of object,issubclass,Super:
#Example 1
class A: # Super class
    def features1(self):
        print("It's working.")

    def features2(self):
        print("It's controled.")

class B(A): # subclass of A
    def features3(self):
        print("It's store data.")

a = A()
a.features1()
a.features1()

b = B()
b.features2()
b.features1()
b.features3()

#Example 2
class food:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f'I love to eat {self.name}.')

class sweat(food):

    def seats_name(self):
        print('And Kheer,Gulab jammun.')

f = food('bryani')
f.display()

s = sweat('x')
s.seats_name()

#Example 3
check = issubclass(sweat,food)
print(check)

c = issubclass(B,A)
print(c)

r = issubclass(A,food)
print(r)
#Example 4
# Using super()
# We can also access parent class members using super.
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f'{self.name} am eating.')
class Dog(Animal):
    def eat(self):
        super(Dog, self).eat()
        print(f'{self.name} eating bones.')

d = Dog('Fido')
d.eat()
# Example 5
class food:
    def name(self,n):
        print(f'i love to eat {n}')
class fo(food):
    def display(self):
        super().name('bryani')
f = fo()
f.display()
# Example 6;
class fun:
    def __init__(self,x):
        self.x = x
    def age(self):
        print(f"MY age is {self.x}")
class sub_class(fun):
    def display(self):
        super().age()

s = sub_class(30)
s.display()
#Example 7
class laptop:
    def name(self):
        print('I have Hp laptop.')
class child_class(laptop):
    def show(self):
        super().name()
c = child_class()
c.show()

