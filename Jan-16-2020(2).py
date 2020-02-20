#!/usr/bin/env python
# coding: utf-8

# In[1]:


list2 = [1, 2, 3, 4, 5, 10, 15, 20, 25, 45, 85, 100]
new_list = []
for i in list2:
    if i > 5:
        new_list.append(i)
print(new_list)


# In[9]:


new_list = []
num_input = int(input("Enter a num >"))
for i in range(1, int(num_input / 2) + 1):
    if num_input % i == 0:
        new_list.append(i)
        new_list.append(num_input)
print(set(new_list))


# In[11]:


common_shit = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in a:
    if i in b:
        common_shit.append(i)
set(common_shit)


# In[ ]:




