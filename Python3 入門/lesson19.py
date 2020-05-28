# Multiple Inheritance

class A:
    def say_a(self):
        print("A!")
    def say_hi(self):
        print("Hi from A")

class B:
    def say_b(self):
        print("B!")
    def say_hi(self):
        print("Hi from B")

class C(A, B):
    pass

c = C()
c.say_a()
c.say_b()
c.say_hi()