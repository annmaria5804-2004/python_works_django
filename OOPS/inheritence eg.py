# #==============2. Inheritance=========================================================

# 2. Inheritance
# =================
# One class can acquire the properties and methods of another class.
# Example: A child class inherits features from a parent class.
# -----------------------------sir-----------------------------------------------------------------
# the one class accquire(can reuse) the method and properties from another class without rewritting it.

class A:
    def method1(self):
        print("Hello")

    def method2(self):
        print("Hello")


class B(A):  # Inheriting class A
    def method3(self):
        print("Hello Python")


# Object creation
obj1 = A()
obj2 = B()

# Method calling
obj1.method1()
obj1.method2()

obj2.method1()
obj2.method2()
obj2.method3()

# Explanation
# - class A – Parent class (Base class).
# - class B(A) – Child class (Derived class).
# - B inherits both method1() and method2() from A.
# - B also has its own method method3().
# Important: The object of class B can access all three methods, but the object of class A cannot access methods belonging only to class B.
#==================================================================================================================================================================

# multiple inheritence-(In multiple inheritance, one child class inherits from two or more parent classes.)-------------------------
# class Child(Parent1, Parent2):
    # methods

class A:
    def method1(self):
        print("Hello")

class B:
    def method2(self):
        print("Hello")


class C(A, B):  # Multiple Inheritance
    def method3(self):
        print("Hello Python")


# Object creation
obj = C()

# Method calling
obj.method1()
obj.method2()
obj.method3()

# Explanation
# - class A – First parent class.
# - class B – Second parent class.
# - class C(A, B) – Child class inheriting from both A and B.
# - method1() – Inherited from A.
# - method2() – Inherited from B.
# - method3() – Own method of C.

#=======================================================================================
# 3. Multilevel Inheritance
# Grandparent → Parent → Child
class A:
    def method1(self):
        print("Grandparent")

class B(A):
    def method2(self):
        print("Parent")

class C(B):
    def method3(self):
        print("Child")

obj = C()
obj.method1()
obj.method2()
obj.method3()

#==============================================================================================
# 4. Hierarchical Inheritance
# One parent → Multiple children 
class A:
    def method1(self):
        print("Hello")

class B(A):
    def method2(self):
        print("Python")

class C(A):
    def method3(self):
        print("Welcome")

obj1 = B()
obj2 = C()

obj1.method1()
obj1.method2()

obj2.method1()
obj2.method3()

#===========================================================================
# 5. Hybrid Inheritance
# Combination of two or more types of inheritance.
class A:
    def method1(self):
        print("A")

class B(A):
    def method2(self):
        print("B")

class C(A):
    def method3(self):
        print("C")

class D(B, C):
    def method4(self):
        print("D")

obj = D()
obj.method1()
obj.method2()
obj.method3()
obj.method4()

#======================================================================
# Type	              Easy meaning
#-------------------------------------------------
# Single	      One parent, one child
# Multiple	      Multiple parents, one child
# Multilevel	  Grandparent → Parent → Child
# Hierarchical	  One parent, multiple children
# Hybrid	      Combination of inheritance type
