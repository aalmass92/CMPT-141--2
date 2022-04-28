# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547

def between(num1, num2,num3):
    """
    between(num1, num2, num3 ) function takes 3 integer arguments and returns True if num2 is between num1 and num3.
    If num2 is not between or if it is equal to other 2 integer arguments it will return false.

    :param num1: integer value
     :param num2:integer value
     :param num3:integer value
      :return: Boolean value
    """

     #condition that indicates the position of the range and returns a boolean value
    if num1 >= num3:

        return num2 in range(num3 ,num1)

    else:
        return num2 in range (num1 +1,num3)
#t = between(-2,2,2)
#print(t)

def majorityEven(num_list):

    """
    majorityEven(num_list) function takes list  of integers and returns True -
    if more than half of the integers are divisible by 2 with no remainder, other it returns False.

    :param num_list: list of integers
    :return: boolean value
    """

    #keep track how many integer values can be divisible by 2 with no remainder
    twoList = 0
    for num in num_list:

        if num % 2 == 0:

            twoList = twoList + 1

    # value that tells you how many are not divisible by 2
    nottwoList= (twoList - len(num_list) )* -1

    #boolean if more than half of the integers are divisible by 2 with no remainder,
    # other it returns False
    return twoList > nottwoList

tlist = [1,2,3,6]
t = majorityEven(tlist)

print (t)
