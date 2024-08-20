#!/usr/bin/env python
# coding: utf-8

# In[1]:


#creating a list
my_list = [1,2,3,4]
print("My list:",my_list)

#Adding an element to the list
my_list.append(5)
print("My list after adding an element:",my_list)

#Removing an element from the list
my_list.remove(1)
print("My list after removing an element:",my_list)

#Modifying an element in the list
my_list[0] = 6
print("My list after Modifying:",my_list)


# In[2]:


# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nInitial dictionary:", my_dict)

# Add elements to the dictionary
my_dict['d'] = 4
print("Dictionary after adding element:", my_dict)

# Remove elements from the dictionary
del my_dict['b']
print("Dictionary after removing element 'b':", my_dict)

# Modify elements in the dictionary
my_dict['a'] = 10
print("Dictionary after modifying element 'a':", my_dict)


# In[4]:


# Create a set
my_set = {0,1, 2, 3}
print("\nInitial set:", my_set)

# Add elements to the set
my_set.add(4)
my_set.update([5, 6])
print("Set after adding elements:", my_set)

# Remove elements from the set
my_set.remove(2)
print("Set after removing element 2:", my_set)

# Modify elements in the set (note: sets do not support indexing)
# Instead, remove the element and add the modified element
my_set.remove(1)
my_set.add(10)
print("Set after modifying element 1 to 10:",my_set)


# In[ ]:




