# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547


import numpy as np



f = open("election_SK_2016.csv", 'r')
masterList2 = [line.rsplit('\n') for line in f]

f.close()

list2 = [x[0:len(masterList2)] for x in masterList2]
list3 = [x[0:len(list2)][0] for x in list2]
list4 = [x[0:len(list3)] for x in list3]
list5 = [x.split(',') for x in list4]
list6 = [x[1:] for x in list5]

constituency = list6[0]
constituencyList = constituency[1:]
#print(constituencyList)

votesListString=list6[1:]

votesList =[[int(j) for j in i] for i in votesListString]

#print(constituencyList)
#print(votesList)

constituencyArray = np.array(constituencyList)
votesArray = np.array(votesList)
#print(constituencyArray[0])
#print(votesArray)

row = len(votesArray[:,0])
#print(col)

totalVoteslist = []

for i in range(row):

     total = sum(votesArray[i])
     totalVoteslist.append(total)

totalVotesArray = np.array(totalVoteslist)

print(constituencyArray)
print(votesArray)
print(totalVotesArray)






