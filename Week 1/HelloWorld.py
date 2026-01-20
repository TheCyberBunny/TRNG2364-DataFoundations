print("Hello, World!")
print('hello world')

##Datatypes in Python
#variables can be declared implicitly without specifying datatype
a = "string of words and characters and yada yada"
explicitString: str = "my explicit string"
#Number types
#Integer - int - whole numbers
b = 7
explicitInt: int = 7
#Float - float - decimal numbers
c = 3.14159
explicitFloat: float = 2.71828

#Boolean - True/False
#Falsey values: 0, 0.0, None, empty string "", empty list [], empty tuple (), empty dict {}
#Truthy values: anything else
d = True
explicitBool: bool = False
if b:
    print("b is True")
else:
    print("b is False")

#Nonetype - None - represents a null value or the absence of a value
e = None
explicitNone: None = None

#print multiple variables
print(a, b)
#print sum of b and c
print(b + c)
#mix data types
print("I have", b, "cats in my house.")

f = 74
print(f)
f = "Green"
print(f)

#Casting  lets us specify the datatype we want to convert to
a = str(9)
b = int(9)
c = float(9) #will print as 9.0
d = bool(9) #will print as True
print(a, b, c, d)

#check datatype using the type() function
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#variables are case sensitive 
A = "uppercase A"
print(A)
a = "lowercase a"
print(a)

#We can assign multiple variables in one line
dog = DOG = Dog = dOg = "Beagle"
print(dog, DOG, Dog, dOg)