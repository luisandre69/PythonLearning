#%% input from user
name=input("What is your name? ")
print("Glad to meet you",name)
#%%
number=input("Write an integer: ")
type(number)
number=int(number)
type(number) #validates that a int was written
#%%
weight=float(input("Whats is your weight? "))
if weight>50:
    print("Your weight is above 50")
elif weight==50:
    print("Your weight is exactly 50")
else:
    print("your weight is below 50")