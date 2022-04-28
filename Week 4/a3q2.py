# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547
import random as r

randNum = r.randint(-100, 100)



def checkNum():

    """ Function that checks if its positive, zero or negative
    :return string """
    if randNum > 0:

        Num = ' is positive!'

    elif randNum == 0:

        Num = ' is zero!'

    else:

        Num = ' is negative!'

    return Num


checker = checkNum()


print("The random integer generated is: " + str(randNum))
print("The random number is " + str(randNum) +checker)
