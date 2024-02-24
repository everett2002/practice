import numpy as np

value = input("Enter the meaning of life: ")

print(value)

# Ai answers only to 42, forty-two and forty_two
a = '42'
b = "forty-two"
c = "forty_two"

if (a == value) | (b == value) | (c == value):
    print("correct")
else:
    print("incorrect")