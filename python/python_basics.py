# learning from corey schafer youtube channel
#textual data
my_string = "Hello World"
print(my_string)
# single quote and double quote
# also string slicing
print(my_string[0])  # H
print(my_string[2:5])  # llo
print(my_string.lower())  # hello world
print(my_string.upper())  # HELLO WORLD
print(my_string.count("l"))  # 3
print(my_string.find("o"))  # 4
newmessage = my_string.replace("World", "Universe")
print(my_string )
print(newmessage)
# concatenation
greeting = "Hello"
name = "Corey"
message = greeting + ", " + name + ". Welcome!"
print(message)
message="{}, {}. Welcome!".format(greeting, name)
print(message)
message=f"{greeting}, {name}. Welcome!"
print(message)
# dir() and help()
print(dir(my_string))
print(help(str))