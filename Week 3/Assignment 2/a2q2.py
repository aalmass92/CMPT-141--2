# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547

def calculate_speed(distance, time):

    """"
    distance : A integer for the number distance in km
    time : A integer for the number of time in hours

    speed: A float calculated from distance over time

    return: the speed from speed over time (km/t), type float
    """
    speed = distance / time
    return speed


print("Calculate Speed")

# user input for distance in km
distance = int(input("Enter desired Distance (km): "))

# user input for time in hours
time = int(input("Enter desired time (hours): "))

# compute the speed from using user input as the arguments
speedValue = calculate_speed(distance, time)

print("In order to travel "+str(distance)+" km in "+ str(time)+" hours you must travel at "+str(speedValue)+" km/h.")
