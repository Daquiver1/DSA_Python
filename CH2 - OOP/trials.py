# Abstract data types(ADT) specify what the operation does but not how.
# In class terminology
# the class parameters or instance variables are called data members.
# the methods are called member functions.
# class names should be capitalized. If two words, it should use CamelCase,
# function names should be a verb. make_payment
# Constants are stored in caps. MAX_SIZE  = 300
# Variables with _before it means ít's nonpublic, so can't acess it directly.
# Dunder methods are short for Double UNDERscore methods
# Dunder methods are __add__, __len__, __init__ and co.
# This is operator overloading in OOP
# If you don't define dunder methods, when you call them on an instance.
# It'll raise an error.
# A subclass differentiates itself from parent class by
# 1. Specalizing an existing behavior. This is overriding.
# 2. By providing new methods. This is Extend
# Shallow copying stores the exact same thing in a different variable but it
# still references the original object.
# So you can delete objects without it affecting the other aliases but if you
# modify, both get modified.
# Deep copying copies the entire thing and pastes it in a different variable,
# so you can do whatever you want
# without fear of modifying the original object.
# You can accomplish this using python's copy module.
