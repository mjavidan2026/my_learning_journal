# append vs extend vs insert : 

my_list = ["hadis", 19, "javidan", 2026]
print("your list : \n " ,my_list)
# ["hadis", 19, "javidan", 2026]


#add 1 item to the end of list ->> append()
my_list.append("mohadeseh")
print("your list after append new item: \n " ,my_list)
# ["hadis", 19, "javidan", 2026, "mohadeseh"]

print("_ _ _ _ _ ")

#adds all items from one list to the end of another list ->> extend()
my_list = ["hadis", 19, "javidan", 2026]
print("this is your list  :\n" ,my_list)
# ["hadis", 19, "javidan", 2026]

my_new_list = ["hello", "python", 3.2]
print("you want add items from this list to your list  :\n" ,my_new_list)
# ['hello', 'python', 3.2]

my_list.extend(my_new_list)
print("your list after extend : \n" ,my_list)
# ['hadis', 19, 'javidan', 2026, 'hello', 'python', 3.2]

print("_ _ _ _ _ ")

#add 1 item at a specific index ->> insert() 

my_list = ["hadis", 19, "javidan", 2026]
print("this is your list :\n" ,my_list)
# ["hadis", 19, "javidan", 2026]

my_list.insert(2 , 2007)
print("your list after inserting item in index 2 :\n" ,my_list)
# ['hadis', 19, 2007, 'javidan', 2026]
