#%%
L=[1,2.0,"bird",10]
L[0]
#%%
L=[1,2.0,"bird",10]
L[1]
#%%
L=[1,2.0,"bird",10]
L[2]
#%%
L=[1,2.0,"bird",10]
L[3]
#%%
L=[1,2.0,"bird",10]
L[-1] #return [10]
#%%List slicing => 
# List[start-index:stop-index:step]
L=[4,5,8,10,20]
L[1:3]  #return [5,8]
#%% ommit start-index will list until the stop index
L=[4,5,8,10,20]
L[:3] #return [4,5,8]
#%% ommit stop-index will list until the stop index
L=[4,5,8,10,20]
L[3:] #return [10,20]
#%%ommit both indices will show the full list
L=[4,5,8,10,20]
L[:]    #return L
#%% + operator concatenates lists
x=[1,2,3]; y=[4,5,6]
x+y #return [1, 2, 3, 4, 5, 6]
#%% * operator repeasts a list a given number of times
[1,3]*3  #return [1, 3, 1, 3, 1, 3]