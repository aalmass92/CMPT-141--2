# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547

def cost():

    """
    Computes the total cost amount for both carpet cost and baseboard plus  labour cost
    :var totalcost_all: calls carpet() function and baseboard() function adds return value with 500 labour cost
    :return: the total cost project
    """
    totalcost_all = carpet(width, length, cost_cpf) + baseboard(width, length, cost_bpf) + 500
    return totalcost_all

def carpet(width,length, cost_cpf):
    """

    Computes the total cost of the carpet
    :param width:  float value for width
    :param length: float value for length
    :param cost_cpf: float value for carpet per foot
    :var area: A float area calculated by width and length parameter
    :var totalCost_carp: A float cost calculated by cost_cpf parameter by area
    :return: the total cost of the carp
    """
    area = width * length
    totalCost_carp = area * cost_cpf

    return totalCost_carp

def baseboard(width,length, cost_bpf):

    """
    Computes the total cost of the baseboard
    :param width:  float value for width by foot
    :param length: float value for length by foot
    :param cost_bpf: float value baseboard per foot
    :var perimeter: calculates perimeter with parameters given
    :return: Total cost baseboard
    """
    perimeter = (2 * width) + ( 2 * length)
    totalCost_bb = perimeter * cost_bpf
    return totalCost_bb

# Ask for user input for function arguments
width = float(input("What is the width of the room (ft) "))
length = float(input("What is the length (ft) "))
cost_bpf = float(input("Input the cost of a linear foot of baseboard ($) "))
cost_cpf = float(input("Input the Cost of a square foot of carpet ($) "))

#call cost() function assign it to variable
totalCost = cost()

print("For a room of width "+str(width)+" and length "+str(length)+" the cost of the reno is $ "+str(totalCost))