# function

def say_hi():
    print("hi")

say_hi()

def say_hi2(name, age = 20):
    print("hi {0} ({1})".format(name,age))

say_hi2("tom",23)
say_hi2("bob",21)
say_hi2("steve")
say_hi2(age = 18, name = "rick")
