## Starting with Python
# This is self-paced. Enjoy
# This file looks at python variables and def function

a = 2
b = 55
first_var = 3

string_variable = "hello"
single_quote_var = 'string with single quote'

#print(a + b)
#print(string_variable)
#print("Hello [there]!")
#print(456)

var1 = "Hey"
var2 = "Hey"

num1 = 6
num2 = 2

### Def function
 
land_animals = ["man", "dog", "cat", "goat", "sheep", "lion"]

def my_print_method(my_parameter):
    print(my_parameter)
my_print_method("Hello, world!")

def my_multiply_method(Numb1, Numb2, Var):
    return Numb1 / Numb2 + 10

result = my_multiply_method(8, 9, 1)
my_print_method(result)

def animals(land_animals):
    print(land_animals)
animals

#def animals_in_water(frog, fish, turtle):
#    print(turtle)
#animals_in_water(1, 3, 5)

def f(y):
    return y**2 + 1
f(4)
