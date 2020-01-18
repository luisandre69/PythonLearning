t = ('a', 'b', 'c', 'd', 'e')
s = (1, 2, 3, 4)

#%% Indexing
print(t[0])

#%% Slicing
print(t[1:3])

#%% Concatenation
print(t + s)

# %% Successive concatenation
print(s * 2)

# %% zip()
A = 'xyz'
B = (1, 2, 3)
list(zip(A, B))

# %% return the index of the value
B.index(3)

# %% return the number of times value occurs in the tuple
B.count(2)

# %% Dictionary
t = [('x', 1), ('y', 2), ('z', 3)]
d= dict(t)
d

# %% returns a list of tuples
d.items()

# %% practical lesson
t1=1,2,3
type(t1)

# %%
t2=(1,2,3)
t3=tuple([1,2,3])
t3[-1]

# %%
t3[1:3]

# %%
t1+t2

# %%
t1*3

# %%
t1='abc'
t2=[1,2,3]
t3='xyz'
list(zip(t1,t2,t3))

# %%
t1.index('c')

# %%
t1.count('a')

# %%
t=[('x1',1),('x2',2),('x3',3)]
d=dict(t)

# %%
d

# %%
d.items()
