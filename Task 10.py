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

#Polymorphism in Pythton:
#Example 1
l = [1,2,34,4]
print(len(l))
                 # Same function of len() work with different type.
s = 'Hello world!'
print(len(s))

#Example 2
# overloading in polymorphism
class A:
    def dispaly(self,name=" "):
        print('My name is '+ name)

obj = A()
obj.dispaly()  # here is not mendetory to pass name its depend
            # on you if you want then pass. overloading concept.
obj.dispaly('ali')

#Example 3
# overriding in polymorphism
class school:
    def display_info(self):
        print("I love my school.")
class student(school):
    def display_info(self):
        super().display_info()
        print("Ali go to school.")
s = student()
s.display_info()      # this is the overriding concept.

# Example 4
a = 4
b = 'Kiran'
print(type(a))
print(type(b))    # type function behave different.

# Example 5
class food:
    def menu(self):
        print('lazaniya,bryani,kheer')
c = food()
c.menu()
#Example 1
#Class/Static variable in Python:
class A:
    age = 20        # Class variable
    def __init__(self):
        self.name = 'Maryam'

    def dispaly(self):
        print(self.name)
a = A()
a.dispaly()
#Example 2
#Class methods and Static methods in Python:
# To access the class variable we used @classmethod.
class A:
    age = 20        # Class variable
    def __init__(self):
        self.name = 'Mhanoor'

    def dispaly(self):
        print(self.name)
    @classmethod     #CLASS METHOD
    def get_age(cls):
        cls.age # Accessing class variable inside class method

a = A()
a.dispaly()
A.age
#Example 3
class Mobile:
    name = 'Oppo'
    @classmethod
    def display(cls):
        print(cls.name)
m = Mobile()
m.display()
Mobile.display()
print(Mobile.name)

#EXample 4
class clg:
    k =10
    @classmethod
    def show(cls):
        print(cls.k)
c = clg
c.show()
#Example 5
class food:
    dish = 'Pulao'    # class variable
    @classmethod #class method
    def repr(cls):
        print(cls.dish) # Accessing class variable
f = food()
print(food.dish)
f.repr()

# Example Changing class members:
# Using the class name change the class member
#Example 1
class Name:
    name = 'Mujhaid'
    @classmethod
    def show(cls):
        print(cls.name)
Name.name = 'Saba'
n = Name()
n.show()

#Example 2
class number:
    num = [1,2,3]
    @classmethod
    def display(cls):
        print(cls.num)
number.num = [23,45,33,22,11]
n = number()
n.display()

#Example 3
class fun:
    game = 'hockey'
    def play(self):
        print(f'we play {self.game}.')
fun.game = 'Football'
f = fun()
f.play()

# Example 4
# Change the  method in class
class Animal:
    name = 'bella!'
    @classmethod
    def cat(cls):
        print(f'I am a {cls.name}.')
a = Animal()
def dog(cls):
    print('I am a dog')
Animal.cat = dog
a.cat()

#Example 5
class A:
    age = 45
    def get_age(self):
        print(self.age)
A.age = 33
a = A()
a.get_age()

#Constructor in Python:
#Example 1
class Constructor:   #when object is crerated then constructor automatically called.
    n = 22
    def __init__(self):  #default constructor
        print(f'The value of n is {self.n}.')

c = Constructor()
#Example 2
class check:
    a = 20
    b = 3
    def __init__(self,x):  # parameterized constructor
        print(f'The value of a is {self.a} and b is {self.b} or value of x is.')
        print(x)
c = check(3)

#Distructor in python:
class Variety_methods:
    def __init__(self):
        print('I am a constructor.')
    def normal(self):
        print('I am a noraml method.')
    def __del__(self):
        print('I am a destructor.')
        print('Object deleted.')
obj = Variety_methods()
obj.normal()
del obj

# example 2
class A:
    def show(self):
        print('I am a display function.')
    def __del__(self):
        print('Object deleted successfully.')
a = A()
a.show()
del a

# Example 3
class fun:
    def __init__(self):
        self.name = 'Kiran'
    def __del__(self):
        print('Deleted name successfully...')
f = fun()

#First class function:
#Example 1
def info():
    print('My name is maryam.')

i = info()
print(i)

#Example 2
def Family(x):
    print(f'Totaly family member is {x}.')
f = Family(6)
print(f)

#Metaprogramming with metaclasses:
#Metaclasses
#Example 1
a = 100
b = 'Amina'
c = 3.5
print(type(a))
print(type(b))
print(type(c))
#Example 2
class Metaclasses:
    pass
m = Metaclasses()
print(type(m))

# Example 3
def A():
    pass
a = A()
print(type(A))

#Class and instance atribute:
#Example 1
class Laptop:
    # class attribute/variable
    name = 'Hp'
    def __init__(self,y):
        #instance attribute/variable
        self.y = y
    def prt(self):
        print(f'I have {self.y}')

    @classmethod
    def display(cls):
        print(cls.name)
l = Laptop('DELL')
l.prt()
l.display()

#Example 2
class Number:
    # class attribute/variable
    num = 70
    def __init__(self,x):
        # instance attribute/variable
        self.x = x
    def show(self):
        print(f'My lucky number is {self.x}.')
    @classmethod
    def get_num(cls):
        print(cls.num)
n = Number(3)
n.show()
n.get_num()

#Reflection:

class Myclass:
    def method_a(self):
        pass
    def method_b(self):
        pass
m = Myclass()
print(dir(m))
# Garbage Collection:
num = 22
num = 26
print(num)
