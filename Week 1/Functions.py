import array #as ar


#Functions are how we package useful functionality into reusable blocks to use when needed

#creating a function - we use the def keyword, name the function, give it parameters
#then we write the code we want it to execute

#function with 2 parameters
def addition_function(x:int, y:int):
    return x + y

#no parameters function
def bark():
    print("woof")

#calling our functions
sum = addition_function(9, 10)
print(sum)
bark()

print(addition_function("my cat", "Wonton"))


#Scopes
#are ares of the ode where an object/variable/function can be called upon and used

#Local: variables declared inside of a block of code and are only available inside that block
def local_variable():
    message = "Hi y'all"
    print(message)

    #Enclosed: function is enclosed within another function
    #This function can access variables from the outer function
    def enclosed():
        message = "enclosed hi y'all"
        print(message)

    enclosed()
    print(message)

local_variable()

#Global: accessed from anywhere within the file they are declared in
#as well as other files IF they are brought in via import
myCat = "Wonton"

#Default: Built in default python methods where all keywords live and can be accessed from anywhere


#Modules in Python are simply files in which python code is written
#to use different modules, we have to import them into the module we want to use it from
#modules also support aliases using the 'as' keyword

#Arrays are not technically built into python, we have to import the array module
#contain elements of the same type, stored sequentially, and indexed from 0
#array(typecode, initializer)

#Typecode: this is a single character that specifies the type of data stored in the array
# 'i' : stored integer (4 bytes)
# 'f' : floating point (4 bytes)
# 'd' : double precision floating point(8 bytes)
# 'b' : signed integer (1 byte)
# 'u' : unicode character (2 bytes)
# 'l' : signed long integer(4 bytes)(platform dependent)

#Initializer: this is an optional parameter that initializes the array with elements
#it can be a list, a tuple, or any other iterable containing the intial values for the array

intArray = array.array('i', [1, 2, 77, 3, 25, 99, 51])
print(intArray[2])
mySubset = intArray[1:4]
print(mySubset)

for item in intArray:
    print(item)

#find the length
print(len(intArray))

#sort array in ascending order
print(sorted(intArray))

#Lambda function AKA anonymous functions
#small, single line functions that can have any number of arguments, but only one single expression
#lambda args: expression

add = lambda x, y: x + y
print(add(3, 4))

Pokedex = [
    ("Bulbasaur", 1),
    ("Lapras", 131),
    ("Eevee", 133),
    ("Cubone", 104),
    ("Gengar", 94)
]
dictionaryPokedex = {2:"Ivysaur", 3:"Venusaur"}
print(Pokedex[1][1])

Pokedex.sort(key=lambda x: x[1], reverse = False)
print(Pokedex)