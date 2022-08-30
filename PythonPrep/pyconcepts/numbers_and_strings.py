'''
    ---- In python the numeric types are created in three ways
        1. int
        2. float
        3. complex //ex:- 6j
'''
import decimal
import random

x = 9               # int
y = 234234.08078    # float
z = 24 + 9j         # complex

print("int type: ", type(x))
print(f"float type: {type(y)}")
print("complex type: ", type(z))
print(f"real word in z: {z.real}")


'''
    ---- Type conversion like
        int(float)
'''

x = 123.3333
print(f"Convert float number to int number: {int(x)}")

'''
    Random number in python
'''
print(random.randrange(2,9))

#   Handel decimals
num1 = '1.1'
num2 = '2.2'
print(decimal.Decimal(num1) + decimal.Decimal(num2))

# math module
number = (3,34,83,2,5,23,54)
print(f"maximum number: {max(number)}")
print(f"maximum number: {min(number)}")
