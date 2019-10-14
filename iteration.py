#%% while loop
x=5
while x>0:
    print(x)
    x=x-1
#%% for loop
for x in range(5,0,-1):
    print(x)
#%% def
def countdown():
    x=10
    while x>0:
        print(x)
        x=x-1
    print("Blast off")
countdown()
#%% def returning x
def countdown1(x):
    for x in range(x,0,-1):
        print(x)
    print("Blast off")
countdown1(8)
#%%
