# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547

# Saskatoon weather for June 2021
# Daily Data in the format [day,high,low]
weather_2021 = [
[1,27.2,7.5],
[2,32,11.3],
[3,34.7,12.5],
[4,27.7,15.2],
[5,27.3,9.9],
[6,18.3,7.5],
[7,22.6,8.3],
[8,23.3,3.4],
[9,19.9,12.2],
[10,22.6,14.2],
[11,19.6,10.3],
[12,24,6.2],
[13,27.2,5.7],
[14,31.8,15.5],
[15,33.8,18.8],
[16,24.2,12.9],
[17,21.2,6.9],
[18,17.3,8.4],
[19,22,6.3],
[20,17.6,4.9],
[21,24.9,0.8],
[22,31,11.5],
[23,24.1,10.2],
[24,25.7,7.2],
[25,27.9,9.7],
[26,29.5,11.6],
[27,27.8,10.8],
[28,30.3,10.6],
[29,34.1,15.1],
[30,35.3,15]
]

# Write your list comprehensions below!

# Part A) - Are any days above 30?
above30Dates = [x[0] for x in weather_2021 if x[1] > 30]
print('(A)\n'+str(above30Dates)+'\n')


# Part B) - List of highs on days when low > 15?
above15highs=[x[1] for x in weather_2021 if x[2] > 15]
print('(B)\n'+str(above15highs)+'\n')

# Part C) - Temperature differences?
tempDiff = [round((x[1]-x[2]),2) for x in weather_2021 ]
print('(C)\n'+str(tempDiff)+'\n')

# Part D) - Weekend Highs?
highSatSun = [(x[0],x[1]) for x in weather_2021 if x[0] % 7 == 5 or x[0] % 7 == 6 ]
print('(D)\n'+str(highSatSun)+'\n')



