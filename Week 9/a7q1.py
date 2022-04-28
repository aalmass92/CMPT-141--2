# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547

import numpy as np


# test1 = [
#     [0, 0],
#     [0, 1],
#     [0, 1]
# ]
# test2 = [
#     [1, 1, 1, 1],
#     [0, 1, 0, 0],
#     [1, 1, 0, 1],
#     [0, 1, 0, 1],
#     [1, 1, 1, 1]
# ]

quizResults = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
]

x = np.array(quizResults)


col: int=len(x[0])


print('Poorly done questions:')
for i in range(col):
    #print (i)
    average = int(sum(x[:, i]) / len(x[:, 0]) * 100)
    #print(average)
    if average < 60:
        print("Only "+str(average)+' percent of students solved question '+(str(i+1)))
