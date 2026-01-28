#In python we can have NAMED tuples
#They allow you to access their elements by name and index
#Named tuples are part of the collections module and provide a way to create
#self-documenting, immutable data structures
#good for reading an object or rows from SQL queries, CSVs, or API responses

from collections import namedtuple, OrderedDict, Counter


#to create a named tuple, we use the namedtuple() factory function
Point = namedtuple('Point', ['pizza', 'y'])

#We can create an instance of Point
p = Point(pizza=1, y=5)
#Access using a field name
print(p.pizza, p.y)

#Access items using index
print(p[0])

#Access using getattr()
print(getattr(p, 'y'))

#more precise example
User = namedtuple("User", ['id', 'username', 'password', 'email'])

myUser = User(12, 'JonDoe', 'password', 'JonDoe@email.com')
mySecondUser = User(88, "jane", "something", 'janesemail@email.com')
print(myUser.username, myUser.password, mySecondUser.username)


#Ordered Dictionaries
#are good for when you are using items in a specific order
#great for configuration settings or environment variables
#also from the collections module

config = OrderedDict()

#set defaults
config["timeout"] = 5
config["retries"] = 3
config["two-factor"] = True

#we can override values that are already set
config["timeout"] = 10

#Set certain items to always be considered last
config.move_to_end("timeout")

#we can inspect the order
for key, value in config.items():
    print(key, value)


#Counters
#counters allow us to count things without writing loops
#comes from the collections module

words = ["fruit", "Meat", "Veggies", "Dairy", "Grains", "Legumes", "fruit", "fruit", "Dairy"]
count = Counter(words)
print(count)

print(count["fruit"])