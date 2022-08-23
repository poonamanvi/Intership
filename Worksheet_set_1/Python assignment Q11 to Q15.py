#!/usr/bin/env python
# coding: utf-8

# # 11. Write a python program to find the factorial of a number

# In[4]:


fact = 1
n = int(input("Enter a number:"))

for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is",fact)


# # 12. Write a python program to find whether a number is prime or composite.

# In[6]:


count = 0
n = int(input("Enter a number:"))

for i in range(1,n+1):
    if n % i ==0:
        count+=1
if count ==2:
    print(n,"is a Prime number")
else:
    print(n,"is a composite number")


# # 13. Write a python program to check whether a given string is palindrome or not.

# In[7]:


str=input("Enter the string to heck Palidrome")
str=str.casefold()
if (str==str[::-1]):
    print("Yes, it is Palidrome")
else:
    print("No,it is not Palidrome")


# # 14. Write a Python program to get the third side of right-angled triangle from two given sides.

# # 15. Write a python program to print the frequency of each of the characters present in a given string.

# In[20]:


str1 = input ("Enter the string: ")
d = dict()
for c in str1:
    if c in d:
        d[c] = d[c] + 1
    else:
        d[c] = 1
print(d)


# In[ ]:




