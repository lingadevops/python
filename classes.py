# class: blueprint for creating objects
# object: instance of a class
#Class 

#class should be start with a capital letter
class Person:
#class can have multiple funtions and each function should have self as the first parameter
    def __init__(self, name, age): #constructor method to initialize the object
        #__init__ is a special method that is called when an object is created