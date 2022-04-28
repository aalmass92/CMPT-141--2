# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547


userInput = input("Please input a string: ")



oddIndex = userInput[0:len(userInput):2]

evenIndex = userInput[1:len(userInput):2]


print("The result by splitting the odd and even part of the input string is: "+oddIndex+','+evenIndex)