
# A variable is a container in memory that stores some data

# Rules for naming a variable:
# 1. Can contain alphabets (a-z, A-Z), digits, and underscore (_)
# 2. Should have a meaningful name (easy to understand what it stores)
# 3. Can start with an underscore, e.g. _variable_name
# 4. Cannot start with a digit or a special character (@, #, $, etc.)
# 5. Cannot contain spaces (use underscore instead, e.g. cms_no not "cms no")


# Storing student information in variables
name = "Fatima"
cms_no = "s24-bscs-0004"
email = "fatimaasalim87@gmail.com"

# Printing multiple variables together with a label
# "\n" is used to move the next value to a new line
print("My name is :", name, "\ncms: ", cms_no, "\nemail: ", email)


# 1. Python is dynamically typed
# You don't need to declare the type of a variable, Python figures it out automatically
age = 21            # Python understands this is an integer
name = "Fatima"      # Python understands this is a string

# 2. A variable's type can change during the program
x = 5         # x is an integer here
x = "Hello"   # now x becomes a string, no error occurs

# 3. Assigning multiple variables in a single line
name, age, city = "Fatima", 21, "Sahiwal"
print(name, age, city)

# 4. Assigning the same value to multiple variables at once
a = b = c = 10
print(a, b, c)

# 5. type() function - checking the data type of a variable
name = "Fatima"
print(type(name))   # <class 'str'>

age = 21
print(type(age))    # <class 'int'>

# 6. Variables are case-sensitive
# Name and name are two DIFFERENT variables
Name = "Fatima"
name = "Aqsa"
print(Name)   # Fatima
print(name)   # Aqsa

# 7. Reserved keywords cannot be used as variable names
# Examples of reserved keywords: print, if, for, class, while, etc.

# 8. Constants (by convention only, not enforced by Python)
# Written in UPPERCASE to show the value should not be changed
PI = 3.14159
print(PI)