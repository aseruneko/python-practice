# map(function, iterator)

def triple(n):
    return n * 3

print(list(map(triple, [1,2,3])))

# lambda 

print(list(map(lambda n: n * 3, [1,2,3])))