# If else conditionals in python
# var1 = 22
var2 = 50
var3 = int(input("Enter the number: "))

if var3 > var2:
    print("The value of var3 is greater than the value of var2")

# elif means else if in python.
elif var3 < var2:
    print("the value of var3 is less than value of var2")

# var1 == 2
# = sign is assignment operator
# == sign is comparision operator
elif var3 == var2:
    print("the value of var3 is equal to the value of var2")

else:
    print("this is else")
