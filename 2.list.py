#Comprehension List 

#list & loop :

my_num = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print("your list :\n" ,my_num)

#your list :
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list_1 = [ num + 2 for num in my_num ]
print("your new list :\n" ,new_list_1)

#your new list :
#  [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("_______")

#loop & condition in list :
my_new_list_2 = [num + 2 for num in my_num if num % 2 == 0]
print(
    "A list of even numbers from the previous list:\n",my_new_list_2
)

print("_______")

my_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print("this is your list :\n ", my_num)

#this is your list :
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_new_list_2 = [ num + 3  if num % 2 == 0  else  num + 1  for num in my_num]

print(
    "we add 3 to even and 1 to odd numbers,\n"
    "The result is:\n", my_new_list_2
)

# we add 3 to even and 1 to odd numbers,
# The result is:
#  [2, 5, 4, 7, 6, 9, 8, 11, 10, 13]


even = [num for num in my_new_list_2 if num % 2 == 0] 
odd = [num for num in my_new_list_2 if num % 2 != 0]

print("Even numbers list :\n",even)

# Even numbers list :
#  [2, 4, 6, 8, 10]

print("Odd numbers list :\n",odd)

# Odd numbers list :
#  [5, 7, 9, 11, 13]