# print('Hello World');   
# print(9*4);


# val = input("");
# print(val);

# num1 = input();
# num2= input();
# print(num1 + num2);



# # input
# string = str(input())
 
# # output
# print(string)
 
# # Or by default
# string_default = input()
 
# # output
# print(string_default)

# Python program showing
# how to take multiple input
# using List comprehension
 
# taking two input at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
 
# taking three input at a time
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)
 
# taking two inputs at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))
 
# taking multiple inputs at a time 
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x) 