#print & return

def print_first_name():
    first_name = "Hadis"
    print(first_name)

print_first_name()
#Hadis
#______________

def print_first_name(first_name):
    print(first_name)

print_first_name("Hadis")
#Hadis


#______________


def print_hello(first_name):
    return "Hello " + first_name

print(print_hello("Hadis"))
#Hello Hadis

#______________

def print_hello_1(first_name_1):
    return "Hi " + first_name_1
print_hello_1(" Hadis")
x = print_hello_1("Hadis")
print(x)

#______________
#print vs return

def add_print(x, y):
    print(x + y)

def add_return(x, y):
    return x + y 

result1 = add_print(5, 3)
#8
print(result1)
#None

add_print(3, 5)
#8

result2 = add_return(5, 3)
print(result2)
#8
print(result2 * 2)
#16
