#%% creating variable
x=50
type(x)
print(x)
x="bird"
type(x) #Dynamic typing
print(x)
x=3.14
type(x)
print(x)
#%%
a,b,c=10,15,20 #assigning multiple values to multiple variables
c
#%% valid and invalid variable names(identifiers)
area circle=314             #invalid because of space
area-circle=314             #invalid because of hythen
area.circle=314             #invalid because of dot
5x=100                      #invalid, starting with the number
global=100                  #invalid, global is keyword
#%% valid identifiers
area_circle=314
_x=10
x5=100
#%% python keywords
import keyword
print(keyword.kwlist)