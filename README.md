
# Python3 Intermediate Level Topics.
# Class,Object,Members.
## Class:
A class in Python is a blueprint for creating objects.
## Object:
An object is a thing that has its own data and can do things. It is like a little computer program in itself.
## Members:
A class can have many members, including

Atributes---->Variables. And

Behaviour---->Methods(function).

If you want to use a methods then mention class name first then method name.

# Data Hiding and Object printing.
## Data Hiding:
In Python, we use double underscore ( __) before the attributes name and those attributes will not be directly visible outside.
## Object printing:
Printing objects give us information about objects we are working with In python, this can be achieved by using __repr__ or __str__ methods.
# Inheritance example of object,issubclass,Super:
## Inheritance:
In heritance is a mechanism in object-oriented programming that allows us to create new classes based on existing classes. This allows us to reuse code and create more complex and specialized classes.
## issubclass():
Issubclass() is a function in Python that returns True if a class is a subclass of another class.
## super:
Super() is a function in Python that allows us to access the methods and attributes of the superclass of a class.
# Polymorphism in Pythton:
The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different in working) being used for different types.
# Class/Static variable in Python:
## Static variables:
Static variables are defined inside the class definition, but outside of any method definitions. They are typically initialized with a value, just like an instance variable, but they can be accessed and modified through the class itself, rather than through an instance.
# Class methods and Static methods in Python:
Class method:
We use @classmethod decorator in python to create a class method.

A class method can access or modify the class state.

A class method takes cls as the first parameter.

Static method:
we use @staticmethod decorator to create a static method in python.

A static method can’t access or modify it.

A static method needs no specific parameters.
# Changing class members:
When you change a class member using the class name, you are changing the value of that member for all instances of that class.
# Constructor in Python:
In Python the __init__() method is called the constructor and is always called when an object is created.
## Types of constructors :
### default constructor:
The default constructor is a simple constructor which doesn’t accept any arguments.
### parameterized constructor:
Constructor with parameters is known as parameterized constructor.
# Distructor in python:

A destructor in Python is a special method that is called when an object is destroyed. It is used to clean up the object and release any resources that it is using.

The destructor is defined using the __del__() method. This method is called automatically when an object is destroyed.
# First class function.
When you assign the whole funtion to any variable.then those variable perform like the assigning function.
# Metaprogramming with metaclasses.
# Metaprogramming:
Metaprogramming in Python is the ability to write code that manipulates code. This can be done using a variety of techniques, including metaclasses.
## metaclasses:
A class also an object.

-> any class declared in python is an object of class 'type'.

-> This 'type' class is called the metaclasses.
# Class and instance atribute:
## Class attributes:
Class attributes belong to the class itself they will be shared by all the instances. Such attributes are defined in the class body parts usually at the top, for legibility.
## Instance atribute:
Unlike class attributes, instance attributes are not shared by objects. Every object has its own copy of the instance attribute (In case of class attributes all object refer to single copy).
# Reflection:
Reflection refers to the ability for code to be able to examine attributes about objects that might be passed as parameters to a function. For example, if we write type(obj) then Python will return an object which represents the type of obj.:
# Garbage Collection:
When a value in a memory is no longer refrenced by a variable, The Python interpreter automatically remove its from memory. This process is known as garbage collection.


