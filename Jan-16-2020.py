#!/usr/bin/env python
# coding: utf-8

# In[4]:


name = input ("Enter name")
year = int(input("Enter year of birth"))
years_lived = 2020 - year
weeks_lived = years_lived * 52
print (f"Hi {name}, you have lived for {weeks_lived} weeks!")


# In[5]:


name = input ("Enter name")
year = int(input("Enter year of birth"))
years_lived = 2020 - year
years_to_hundred = 100 - years_lived
print (f"Hi {name}, you will celebrate your 100th birthday in {years_to_hundred} years!")


# In[8]:


num1 = int(input("Enter 1st num > "))
num2 = int(input("Enter 2nd num > "))
if num2 == 0:
    print("Cannot divide by 0 !!")
else:
    num3 = num1 / num2
    print(f"The quotient is {num3}")
    


# In[13]:


name = input ("Enter name")
year = int(input("Enter year of birth"))
years_lived = 2020 - year
weeks_lived = years_lived * 52
print (f"Hi {name}, you have lived for {years_lived} years or {weeks_lived} weeks!")
if years_lived > 65:
    print(f"Hey {name} man, you're a senior")
elif years_lived > 50 and years_lived <= 65:
    print("Hey you're getting to be a senior !!")
else:
    print(f"Hey {name}, you're a Junior!")


# In[16]:


import math
num1 = int(input("Enter a num > "))
square_root = math.sqrt(num1)
rounded_sqrt = round(square_root, 2)
print(f"The square root of the num is {rounded_sqrt}.")


# In[18]:


a = int(input("Enter a num > "))
b = int(input("Enter b num > "))
c = int(input("Enter c num > "))
D = math.sqrt(b*b - 4*a*c)
if D > 0:
    root1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    root2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
    print(f"The roots are {root1} and {root2}")
else:
    print("ERROR")


# In[21]:


#lists
my_list = [1, 2, 3]
print(my_list)
my_list.append(4)
print(my_list)


# In[23]:


my_list[-1]


# In[24]:


len(my_list)


# In[28]:


my_list[2:3]


# In[29]:


nest = [1, 2, [3, 4]]
nest[2]


# In[30]:


for x in my_list:
    print(x)


# In[31]:


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1


# In[ ]:


list2 = [1, 2, 3, 4, 5, 10, 15, 20, 25, 45, 85, 100]
sum = 0
i = 0
while i < len(list2):
    sum = sum + list2[i]
average = sum / len(list2)
max_num = max(list2)
min_num = min(list2)
print (f"Sum = {sum}, Average = {average}, Maximum is {max_num}, and Minimum is {min_num}")


# In[ ]:


list2 = [1, 2, 3, 4, 5, 10, 15, 20, 25, 45, 85, 100]
new_list = []
for i in list2:
    if i > 5:
        new_list.append(i)
print(new_list)


# In[ ]:




