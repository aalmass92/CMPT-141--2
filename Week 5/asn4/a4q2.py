# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547




while True:
    h = int(input("Enter half life in days: "))
    if h > 1:
        break
    else:
        print("Error! Half life must be a positive number.")

while True:
    m = int(input("Enter initial amount of material in grams: "))
    if m > 1:
        break
    else:
        print("Error! mass must be a positive number.")




#print(remainMass)
t = 0
remainMass = m * (0.5 **(t/h))
onePer = m * 0.01

#print("After "+ str(t) +' days there are '+ str(remainMass)+ ' grams remaining.')


while True:
    remainMass = m * (0.5 ** (t / h))
    print("After "+ str(t) +' days there are '+ str(remainMass)+ ' grams remaining.')

    t = t + 1

    if remainMass < onePer:
        break

