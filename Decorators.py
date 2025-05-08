'''
✅ 1. What / Why / When / How
What is a decorator?
A decorator is a function that modifies or enhances another function without changing its code.

✅Why use it?
For code reuse, logging, access control, timing, etc.
Keeps your code clean, DRY (Don't Repeat Yourself), and modular.

✅When to use it?
When you want to add the same behavior to multiple functions (like logging or checking permissions).
Example: In web apps (Flask/Django), command-line apps, or testing.
-------------------------------------------------------------------------------------------------------
✅3. Built-in Decorators
Python comes with ready-to-use decorators:

@staticmethod: Method belongs to the class, no need for self.

@classmethod: Receives the class (cls) instead of the instance.

@property: Turns a method into an attribute.

@setter and @deleter: Used with @property to allow changing or deleting the attribute.
--------------------------------------------------------------------------------------------------------
✅ 4. Decorator with Arguments
You can pass arguments to a decorator by adding one more layer of functions.

Needs 3 nested functions:

Outer function: takes the decorator arguments.

Middle function: takes the actual function to be decorated.

Inner function: the wrapper.
--------------------------------------------------------------------------------------------------------
✅ 5. functools.wraps
When you use a decorator, the original function’s name and docstring are lost.

functools.wraps is used to keep original metadata.
---------------------------------------------------------------------------------------------------------
✅ 6. Multiple Decorators
You can stack multiple decorators on one function.

@decorator1
@decorator2
def func():
    pass

#They are applied from bottom to top:
      decorator2 wraps func
      Then decorator1 wraps the result
---------------------------------------------------------------------------------------------------------
'''
#Basic example of an Decorator:

def wow_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper 
@wow_decorator
def hehe():
    print("HEHE")
hehe()
