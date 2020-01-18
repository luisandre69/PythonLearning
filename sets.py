#%%
x=set([1,2,3,4,5])
x

#%%
# set(([1,2],[3,4]))

#%% all elements from sets are distinct
Cities=set(("Calcutta","New Delhi", "Chenai", "Mumbai", "Calcutta"))
Cities
#%%
temperature={"High","Moderate","Cold"}
temperature

#%% 
x = set([1,2,3,4,5])
x.add(100)
x

#%%
x.add(5)
x

#%%
x.pop()

#%%
x.clear()
x

#%% set difference
all={1,2,3,4,5,6,7,8,9}
par={2,4,5,8}
impar = all - par
impar

#%% set union
par | impar

#%% set intersection
all & set([2,3,12])
