#%%
temperature_celsius = 5
if temperature_celsius>25:
    print("Weather is hot")
elif temperature_celsius > 15:
    print("Weather is moderate")
elif temperature_celsius>=10:
    print("Weather is nice")
else:
        print("Weather is cold")
#%% conditionals
x=24
if x%2==0:
    print("Even number")
else:
    print("Odd number")
#%% Chained Conditional
temp=7
if temp>20:
    print("It is hot")
elif temp>15:
    print("It is moderate")
elif 10<temp<=15:
    print("It is nice")
else:
    print("It is cold")
#%% Nested conditional
x=6
if x%2==0:
    if x%3==0:
        print("x is divisible by both 2 and 3")
#%% Conditional with compound boolean expression
x=30
if x%2==0 and x%3==0 and x%5==0:
    print("x is divisible by 2,3 and 5")


#%%
