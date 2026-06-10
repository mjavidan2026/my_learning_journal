# Global & Local Variable

y = 4 #global
print("global variable at the beginning: ", y) 
# global variable at the beginning: 4


def func_a ():
    print("variable in func a: ", y)
func_a() 
#variable in func a: 4


def func_b ():
    y = 8 #local
    print("variable in func b: ", y)
func_b() 
#variable in func b: 8


print("global variable after local assignment in func b:", y) 
# global variable after local assignment in func b: 4


def func_c ():
    global y
    y = 10
    print("variable in func c:", y)
func_c() 
#variable in func c: 10


print("global variable after global assignment in func c:", y) 
# global variable after global assignment in func c: 10