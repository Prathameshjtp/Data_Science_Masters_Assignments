#!/usr/bin/env python
# coding: utf-8

# Q1. How do you comment code in Python? What are the different types of comments?

# In[ ]:


#In Python, you can write comments using the '#' symbol. Anything after the '#' symbol on a line is considered a comment and is ignored by the Python interpreter.
#1.Single-line comments: These comments are used to add explanations or notes within a single line of code. They start with the '#' symbol and extend until the end of the line.
#Multi-line comments: Although Python doesn't have built-in multi-line comment syntax like some other languages (e.g., /* */ in C/C++), you can achieve multi-line comments by using triple quotes (''' or """). Anything within triple quotes is treated as a string literal and ignored by the interpreter.
#we can also use triple quotes as a docstring, which is used to document modules, classes, functions, or methods. While docstrings serve a similar purpose to comments, they are accessible through Python's built-in help() function and can provide documentation for your code.


# Q2. What are variables in Python? How do you declare and assign values to variables?

# In[ ]:


#In Python, variables are used to store data values. They act as containers for storing different types of data, such as numbers, strings, lists, or more complex data structures like dictionaries or objects. Variables in Python do not require explicit declaration to reserve memory space. The declaration happens automatically when a value is assigned to a variable.
# Variable declaration and assignment
variable_name = value

# Examples
x = 5         # Assigning an integer value to a variable named 'x'
name = "John" # Assigning a string value to a variable named 'name'
pi = 3.14     # Assigning a float value to a variable named 'pi'

# Multiple assignments
a, b, c = 1, 2, 3  # Assigning multiple values to multiple variables in a single line

# Variable reassignment
x = 10        # x is reassigned with a new value


# Q.3 How do you convert one data type to another in Python?

# In[ ]:


#In Python, you can convert one data type to another using type conversion functions or constructors. 
#1.Implicit Type Conversion: Python automatically converts one data type to another if it makes sense. For example, adding an integer to a float will result in a float.
#2.Explicit Type Conversion (Type Casting): You can explicitly convert data types using type conversion functions or constructors. These methods allow you to convert data types explicitly, which is useful when you want to be specific about the conversion.

int(): Converts a value to an integer.
float(): Converts a value to a float.
str(): Converts a value to a string.
bool(): Converts a value to a boolean.
    
#3.Using constructor functions: For some data types, you can use constructor functions directly to convert values. For example, list(), tuple(), dict(), etc.
# Using constructor functions for conversion
my_list = list((1, 2, 3))  # Convert a tuple to a list
print(my_list)            # Output: [1, 2, 3]

my_tuple = tuple([4, 5, 6])  # Convert a list to a tuple
print(my_tuple)             # Output: (4, 5, 6)


# Q4. How do you write and execute a Python script from the command line? 

# In[ ]:


#Write Your Python Script: Create a text file with your Python code. Save it with a ".py" extension.

#Open Command Prompt or Terminal: Go to the directory where your Python script is saved.

#Execute the Script: Type python (or python3 on some systems) followed by the name of your script file and press Enter.

#View the Output: The script will run, and any output will be displayed in the command prompt or terminal window.


# Q5.Given a list my_list = [1,2,3,4,5], write the code to slice the list and obtain the sub-list [2, 3].

# In[1]:


my_list = [1, 2, 3, 4, 5]

# Slicing to obtain the sub-list [2, 3]
sub_list = my_list[1:3]

print(sub_list) 


# Q6. What is a complex number in mathematics, and how is it represented in Python?

# In[ ]:


#Complex numbers are used to represent quantities that have both a real and an imaginary component, such as electrical impedance, quantum mechanics, signal processing, and more.
#In Python, complex numbers are represented using the complex() constructor or by using the notation a + bj, where a represents the real part and b represents the imaginary part. The imaginary unit is denoted by j in Python instead of i.
# Using the complex() constructor
z1 = complex(2, 3)  # 2 + 3i
z2 = complex(-1, 5)  # -1 + 5i

# Using the notation a + bj
z3 = 1 + 2j  # 1 + 2i
z4 = -3 - 4j  # -3 - 4i

print(z1)  # Output: (2+3j)
print(z2)  # Output: (-1+5j)
print(z3)  # Output: (1+2j)
print(z4)  # Output: (-3-4j)


# Q7. What is the correct way to declare a variable named age and assign the value 25 to it?

# In[3]:


#The correct way to declare a variable named age and assign the value 25 to it in Python is as follows:
age = 25


# Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable
# belong to?

# In[ ]:


#When you declare a variable named price and assign the value 9.99 to it in Python, it belongs to the data type called float.
price = 9.99


# Q9. Create a variable named name and assign your full name to it as a string. How would you print the
# value of this variable?

# In[4]:


name = "Prathamesh Jagtap"
print(name)


# Q10. Given the string "Hello, World!", extract the substring "World".

# In[5]:


original_string = "Hello, World!"
substring = original_string[7:12]
print(substring)


# Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are
# currently a student or not.

# In[ ]:


is_student = True  # If you are currently a student
is_student = False  # If you are not currently a student

