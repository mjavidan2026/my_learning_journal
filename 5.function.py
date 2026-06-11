#mutable & immutable variables in function :

numb = 3
#immutable
print("your initial number:" ,numb)
#3


def change_numb(your_numb):
    your_numb += 1
    print("new value of number after function operation: 3 + 1 = " ,your_numb)
change_numb(numb) 
#4


#Result: The original number remains unchanged - int are immutable.
print("your number after operation:" ,numb )
#3


print("-------")

my_list = [1, 2, 3]
#mutable
print("your initial list:" ,my_list)
#[1, 2, 3]


def change_list (your_list):
    your_list.append(4) 
    print("new list after function operation:" , your_list) 
change_list(my_list)
#[1, 2, 3, 4]


#Result: The original list remains changed - list are mutable.
print("your list after operation:" ,my_list )
