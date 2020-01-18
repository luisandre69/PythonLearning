#%%
Age= {"Partha":48, "Sanjay":39, "Suchi": 23}
Age["Suchi"]

# %%
Age["Gourav"]=19
Age

# %% checking membership
'Gourav' in Age

# %% increasing the value associated with the key
Age["Gourav"]+=1
Age["Gourav"]

# %% length of dictionary
len(Age)

# %% Deleting entry
del Age["Partha"]
Age

# %% Know the keys of the dictionary
Age.keys()

# %% Know the values of the dictionary
Age.values()

# %%
