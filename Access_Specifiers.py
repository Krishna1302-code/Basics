'''
🔐 What Are Access Specifiers?
Access specifiers control who can access what — for example:
#Should this variable be accessible only inside the class? Or is it okay to access it from outside or in subclasses?
#languages like Java and C++ enforce this strictly using public, private, and protected.

🐍 Why Not in Python?
Python doesn't have strict access specifiers because of its design philosophy:

👉 "We are all adults here."
This means:
 Python trusts the developer to do the right thing.
 Instead of blocking access, it uses naming conventions to indicate intent.

 🧠 Access Specifier Conventions in Python
 
| Convention   | Meaning                           | Example       |
| ------------ | --------------------------------- | ------------- |
| `public`     | Anyone can access it              | `self.name`   |
| `_protected` | Meant for internal use/subclasses | `self._name`  |
| `__private`  | Hidden with name mangling         | `self.__name` |


But remember: all of these can technically still be accessed.

🔍 So Why Use Them at All?
Even though Python doesn’t enforce access control:
    #These conventions guide other developers
    #Help in maintaining code structure
    #Support encapsulation (a core part of OOP)

✅ Summary (Easy Version)

Python has no real access specifiers (no keywords like private, public)
Instead, it uses:

      name → public
     _name → protected (convention)
     __name → private (name mangling)

This supports clean design but leaves control in your hands


'''