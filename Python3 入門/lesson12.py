msg = "hello" # global variable

def say_hi():
    global msg
    msg = "hi"
    print(msg)

say_hi()
print(msg)