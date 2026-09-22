# Function Definition
m = 100
print(f"Globally Value of m: {m}")
def add(a,b):
    m = 25
    print(f"locally Values of a,b in add: {a},{b}")
    print(f"locally Value of m in add: {m}")
    return a+b

def sub(a,b):
    print(f"locally Values of a,b in sub: {a},{b}")
    print(f"locally Value of m in sub: {m}")
    return a-b

a = 89
b = 100
print(f"Globally Values of a,b: {a},{b}")
print(add(10,20)) # Function Call
print(sub(50,20)) # Function Call
print(f"Globally Value of m: {m}")
# m = 700