#lets learn the basic in oops in python 
'''
Classes and Objects are core concepts that exist throughout OOP 
— not just in inheritance. They are the foundation of Object-Oriented Programming in Python and are used in every OOP concept
(including Inheritance, Encapsulation, Polymorphism, and Abstraction).
'''
class try1:

    def __init__(self,name,title):#Constructor: runs automatically when object is created.
        self.name=name
        self.title=title 
        print(f"Her name is {name} and her job is {title}")
    def show(self):
        print("\n This is method of class try1 from method show:")

demo=try1('Krishna','Fashion designing')
demo.show()

'''
💬 Why are we passing values?
Because when we create the object, the __init__() function (constructor) needs those values to give your object its unique identity.
Without passing values, Python won’t know:
what name to assign
what job to assign

🎯 Summary:
We do this to create customized objects based on the class blueprint. Without giving inputs, the class can’t generate real-world examples.
'''