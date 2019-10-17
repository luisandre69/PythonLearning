#%% List.insert(i,x)
L=[1,2,3]
L.insert(0,100)
L   #[100,1,2,3]
#%% List.append(x)
L=[100,1,2,3]
L.append(500)
L   #[100,1,2,3,500]
#%% List.remove(x)
L=[100,1,2,3,500]
L.remove(500)
L   #[100,1,2,3]
#%% List.pop([i])
L=[100,1,2,3]
L.pop(1)
L   #[100,2,3] removes i posiiton
#%% List.pop()
L=[100,1,2,3]
L.pop()
L   #[100,1,2] removes last element
#%% List.extend(seq)
L=[1,2,3]
L.extend([4,5,6])
L   #[1,2,3,4,5,6]
#%% List.index(x)
L=[1,2,3,3,2,1]
L.index(3)
L
#%% List.count(x)
L=[1,2,3]
#%% List.sort()
L=[1,2,3]
#%% List.reserver()
L=[1,2,3]
#%% sorted(List)
L=[1,2,3]
#%%
l=[1,2,3]
l.insert(0,100)
l.append(500)
l.remove(500)
l.pop()
l
#%%
l=[100,1,2]
l.extend([3,4,7,5,6,7])
l.count(7)
#%%
l=[100, 1, 2, 3, 4, 7, 5, 6, 7]
l.sort(reverse=True)
l
#%%
l=[100, 7, 7, 6, 5, 4, 3, 2, 1]
l.reverse()
l