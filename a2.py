# 1) Create variables to store different types of values:
#    - `name` as text (string)
#    - `age` as a whole number (integer)
#    - `is_student` as True/False (boolean)
#    - `weight` as a decimal number (float)
name="Arshita"
age=11
is_student=True
weight=30.3
# 2) Print each variable’s value.age

print ("name=",name)
print ("age=",age)
print ("is_student=",is_student)
print ("weight=",weight)
# 3) Print the datatype of each variable using `type()`.
print ("name type=",type (name))
print ("age type=",type (age))
print ("is_student type=",type (is_student))
print ("weight type=",type (weight))
# 4) Show a message that type casting will happen next.
print ("after type casting")
# 5) Convert `age` from an integer to a string and store it back in `age`.
age=str (age)
# 6) Print `age` and print its datatype again to confirm it changed.
print ("age type is",type(age))
# 7) Convert `weight` from a float to an integer and store it back in `weight`.
weight=int (weight)
# 8) Print `weight` and print its datatype again to confirm it changed.
print ("weight is",type (weight))