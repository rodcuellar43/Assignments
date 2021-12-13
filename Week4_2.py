#!/usr/bin/env python
# coding: utf-8

# # Week 4 (Mon) - Logic Practice

# Write a Python program to get next day of a given date.
# 
# Here is a logic flowchart to help

# ![python-conditional-exercise-41.png](attachment:python-conditional-exercise-41.png)

# In[4]:


year = int(input("Input a year: "))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))


# ## Exercise \#1

# Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# ![python-conditional-exercise-10.png](attachment:python-conditional-exercise-10.png)

# In[23]:


for x in range(1,51):
    if x % 3 == 0 and x % 5 == 0:
        output = "fizzbuzz"
    elif x % 3 == 0:
        output = "fizz"
    elif x % 5 == 0:
        output = "buzz"
    else:
        output = x
    print(output)


# ## Exercise \#2
# 
# Write a Python program to calculate a dog's age in dog's years. 
# 
# *Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.*

# In[1]:


h_age = int(input("Input a dog's age in human years: "))

if h_age < 0:
    print("Age must be positive number.")
    exit()
elif h_age <= 2:
    d_age = h_age * 10.5
else:
    d_age = 21 + (h_age - 2)*4

print("The dog's age in dog's years is", d_age)


# ## Exercise \#3
# 
# Write a Python program to check whether an alphabet is a vowel or consonant.

# In[2]:


ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")


# ## Exercise \#4
# 
# Write a Python program to check a triangle is equilateral, isosceles or scalene. 
# 
# *Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.*

# In[3]:


print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")


# ## Exercise \#5 
# 
# Write a Python program to convert temperatures to and from celsius, fahrenheit. 
# 
#  Formula : c/5 = f-32/9 ; 
#  where c = temperature in celsius and f = temperature in fahrenheit 

# In[ ]:


temp = input("Input the  temperature you like to convert?")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")


# In[ ]:




