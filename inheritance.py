'''
🔹 What is Inheritance?
Inheritance allows a class (called a child or subclass) to acquire the properties and behaviors (methods and attributes) of another class (called a parent or superclass).

🧠 Why use Inheritance?
Code reuse – Write once, use in multiple classes.
#Hierarchy – Model real-world relationships (e.g., Dog is an Animal).
#Extensibility – Add or override functionality easily.

Types of Inheritance in Python:

🔹 1. Single Inheritance
One child inherits from one parent.
---------------------------------
Eg-
class Parent:                                        
    pass

class Child(Parent):
    pass
--------------------------------
Parent
  │
  ▼
Child
------------------------------------------------------------------
------------------------------------------------------------------

🔹 2. Multilevel Inheritance
A class inherits from a child class (grandparent → parent → child).
---------------------------------------------------------------------
Eg-
class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass
----------------------------------------------------------------------
Grandparent
     │
     ▼
   Parent
     │
     ▼
   Child
----------------------------------------------------------------------
----------------------------------------------------------------------
🔹 3. Multiple Inheritance
One child inherits from more than one parent.
---------------------------------------------
Eg-
class Mother:
    pass

class Father:
    pass

class Child(Mother, Father):
    pass
---------------------------------------------
Mother   Father
   │        │
   └──┬─────┘
      ▼
    Child
---------------------------------------------------------------------
---------------------------------------------------------------------

🔹 4. Hierarchical Inheritance
Multiple child classes inherit from one parent.
----------------------------------------------------
class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass
----------------------------------------------------
       Parent
       /    \
      ▼      ▼
  Child1   Child2
----------------------------------------------------------------------
----------------------------------------------------------------------
🔹 5. Hybrid Inheritance
Combination of two or more types.
----------------------------------------
class A:
    pass

class B(A):
    pass

class C:
    pass

class D(B, C):
    pass
----------------------------------------
    A       C
    │       │
    ▼       ▼
    B       │
     \     /
      ▼   ▼
        D
----------------------------------------------------------------------
----------------------------------------------------------------------
'''

'''
#1 Single level inheritance
class mother:
    name=None
    def get(self,name):
        self.name=name
        
    def show(self):
        print(f"My name is {self.name} and form Mother class")
m=mother()
m.get('Krishna')
m.show()
'''

'''
'''
'''#2 Multilevel inheritance
class Grandparents():
    paisaa=None
    def jaidaat(self):
        print("Grandfather:Meri jaidaat he")
class Parents(Grandparents):
    Nopaisa=None
    def khud_ke_paise(self):
        print("Parents:Mere paise")
class genZs(Parents):
    influencers=None
    def Social_media(self):
        print("genZs:Its not givining")

p=Parents()
p.jaidaat()
g=genZs()
g.khud_ke_paise()

'''
'''
'''
#3 Multiple Inheritance
class A:
    def show(self):
        print("This is from Class A")
class B:
    def show1(self):
        print("This is from class B")
class C(A,B):
    def show2(self):
        print("This is from class C")
a=A()
b=B()
c=C()
c.show()
c.show1()
c.show2()
    


