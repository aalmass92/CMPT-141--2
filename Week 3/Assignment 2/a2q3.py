# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547

def fence_cost(width, length, height, cost ):

    """ Computes the total cost of 3 sided fence with  inside and outside area

        area: a float calculated from width, height and length given.

        total_area: a float calculated by area calculated by 2 because inside and outside

        totalCost: a float calculated by total_area by cost

        return: return of totalCost
    """

    area = ((width)* height) + ((2 * length)* height)
    total_area = area * 2
    totalCost= total_area * cost

    return totalCost

# User input for arguments
width = float(input("Enter the width of the fence area in meters: "))
length = float(input("Enter the length of the fence area in metres: "))
height = float(input("Enter the height of the fence in metres: "))
cost = float(input("Enter the cost of paint per square metre: "))

# function call with arguments
totalFenceCost = fence_cost(width,length,height,cost)


print("The fence will cost $"+str(totalFenceCost)+" to paint.")