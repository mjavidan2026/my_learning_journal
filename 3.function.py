#4 Types of function based on "inputs" & "outputs" :

#1.NO "inputs", NO "outputs"
def in_out_put_1():
    print("In this func we dont have inputs and outputs")

in_out_put_1()


#2.NO "inputs", WITH "outputs"
def in_out_put_2():
    return "In this func we dont have inputs"

print(in_out_put_2())

#3.WITH "inputs", NO "outputs"
def in_out_put_3(x):
    print(x) 

in_out_put_3("In this func we dont have outputs")


#4.WITH "inputs", WITH "outputs"
def in_out_put_4(x): 
    return x 

print(in_out_put_4("In this func we have inputs and outputs"))
 