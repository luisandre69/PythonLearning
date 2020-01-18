# %% IndexError
L=[1,5,8]
L[3]

# %% KeyError
x={"a":1,"b":2,"c":3}
x["d"]

# %% TypeError
L=[1,2,3,4]
L["a"]


# %% AttributeError
L=[1,2,3,4]
L.add(5)

# %% NameError
z

# %% ZeroDivisionError
y=10/0
y

# %% IndentationError
def greet():
    print("Hello")

# %% OverflowError
a=24583**2456.1245
a