

# print() -> display output  
print("hello") # hello

# arithmetic operation
print(2 + 3) # 5

# substraction  
print (5-2)


# multiplication
print (2*5)

# division
print (10/2) #true division produces a float 5.0
print (10//2) #floor division rounds down to the nearest whole number (interger)

# modulus %
print(9%2) # 1

# variables in python 
# rules for assigning variable names 
# 1. variable name should start with a letter 
# 2. variable name shouldn't start with a number 
# 3. variable name can only contain alpha-numeric characters


# variable_name assignment op          value
var                      =         100
print(var)

name = "python"

print(name)


# PYTHON DATA TYPES 
# TWO MAIN TYPES  
# 1. Primitive data types 
# 2. Data structures/ containers 


# 1. Primitive data types 
    #    -> hold single value 

# a. integer
num_val = 10 
print(num_val)

# b. float 
float_val = 10.0

# c. string -> characters and in quotes 
name = "python"

# d. boolean -> represented by True or False 
is_true = True 

# e. None datatype 
nothing = None 
print(nothing)

print("\n")
# 2. Data structures/ containers 
     # -> hold multiple values 
# a. list 
# b. tuple 
# c. set 
# d. dictionary 


# a. list -> ORDERED collection of elements
        #   -> represented with []

          # 0    1    2     3         4
list_val = [1, True, None, "python", 10.0]

# indexing a list  
print(list_val[4])

# slicing a list 
print(list_val[0:3])
print(list_val[2:5
])

# methods in a list  
# print()  -> display output 
#          -> function 
# list()   -> list 
    #   -> function specific to a data type  

# .append() -> add a value to the end of the list 


# .insert(index, value) -> add a value at a specific index
list_val.insert(3,1000)
print(list_val)


# .pop() -> remove the last value 
list_val.pop()
print(list_val)

list_val.pop(1)  # provide index

print(list_val)

# .remove() -> remove a value 
list_val.remove(None)  # provide value

print(list_val)


print("\n")  # newline 
# Reassignment in a list  
    # -> index the value 
    # -> assign a new value
print(list_val[0])
list_val[0] = "Mango"

print(list_val)

# NESTED LIST -> list withing a list  
                #  0         1             2
                                  # 0   1      2
nested_list = ["apple", "banana", [12, 67, "grapes"]]

# indexing a nested list  
print(nested_list[2][2])

# slicing a nested list 
                    #  [67, "grapes"]

print(nested_list[2][1:3])


# Reassignment in Nested list 
# reassign 67 with coconut  
nested_list[2][1]= "coconut"
print (nested_list[2][1])


# b. tuple -> ORDERED collection of elements
        #  -> IMMUTABLE -> cannot be changed
        #  -> represented with ()

print("\n")
             #-5   -4    -3        -2     -1
tuple_val = (1, True, None, "apple", 198.0)

# indexing a tuple  
            #    198.0  
print(tuple_val[4])
print(tuple_val[-1])


# slicing a tuple 
            # None, "apple"
print(tuple_val[2:4])

# reassignment error for tuple 
# tuple_val[0] = 1000
# print(tuple_val)


tuple_fruits = "watermelon", "guava", "grapes"
print(tuple_fruits)

num_value = 45,

print(num_value)


# tuple unpacking  

# a =  20 
# b =  90
a, b = 20, 90

print(a)



# c. dictionary -> UNORDERED collection of items (key-value pairs)
              # -> represented with {}

print("\n")
# key -> value
                # 0  -> key
list_vals = ['value1']

dict_val = {2: 'value1', 
            "name": 'Python'}

# indexing a dictionary a
print(dict_val[2])
print(dict_val['name'])


# Reassignment in dictionary/ update a key's value
# list_val[0]  = "mango"
dict_val[2] = "coconut"
print("new dict_val", dict_val)


# adding a new key-value 
dict_val['car'] = 'subaru'

print("adding new key-value", dict_val)

print("\n")
# Dictionary methods 
# method -> function specific to a data type (i.e dictionary)

# .keys() 
print("keys in the dictionary: ", dict_val.keys())

# .values()
# type here  
print("values in the dictionary: ", dict_val.values())

# .items()-> both keys and values in tuple format
print("items in the dictionary: ", dict_val.items())

# .pop() 
print("pop() in the dictionary: ", dict_val.pop('name'))

# .update() 
dict_val.update({'car':'Toyota'})
print("updated dict: ", dict_val)

# .get() 
# print("indexing a dict: ", dict_val['car'])
print("indexing a dict: ", dict_val.get('car'))


# Nested dictionary - dictionary inside a dictionary

nested_dict = {3: {'innerkey': [90, 45, 'pineapple']}, 
               'fruit': ('orange', 'apple')
                }
print("nested dictionary output: ", nested_dict[3])
            #    {'innerkey': [90, 45, 'pineapple']}

print("nested dictionary output: ", nested_dict[3]['innerkey'])
                # [90, 45, 'pineapple']  -> list

print("nested dictionary output: ", nested_dict[3]['innerkey'][-1])
                #    'pineapple'

# reassign pineapple
nested_dict[3]['innerkey'][-1] = 'orange'


# output 'apple'
print(nested_dict['fruit'][-1])


# sets -> UNORDERD collection of UNIQUE items 
#      -> {}
print("/n")

list_example = [2, 2, 3, 3, 67, 8]
print("list examples: ", list_example)
set_example = {2, 2, 3, 3, 67, 8}
print("set examples: ", set_example)

# methods in a set 
# .update 
set_example.update([300, 900])
print("updated set values: ", set_example)

# .add()
set_example.add("orange")
print("adding set values: ", set_example)


# .remove()
set_example.remove("orange")
print("removing values: ", set_example)

# .discard()
set_example.discard("orange")
print("dicarding values: ", set_example)


# next session 
# comparison op / logical op 
# branching in python (if-elif-else)
        # nested if statements 
# loops (for & while loops)










