# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547

def maximumScoreFrom ( track , loc ):
    '''
    Calculate the maximum score that Olly can get from stepping and jumping
    along the given track , starting at the given location
    : param track : a list of integers
    : param loc : an index representing Olly ’ current location
    : return : an integer representing the maximum score Olly can get
    '''
    # terminating condition
    if loc == len(track) - 1:
        return 0
    foundJump = False
    if loc + 3 <= len(track)-1:
        jumpscore = maximumScoreFrom(track, loc + 3)
        foundJump = True
    if loc + 1 <= len(track)-1:
        stepscore = maximumScoreFrom(track, loc + 1)
        if foundJump:
            return track[loc] + max(jumpscore, stepscore)

    return track[loc] + stepscore

easy = [0 , -1 , -1 ,1 , -1 , -1 ,0]
medium = [0 , -1 ,1 , -1 , -1 ,1 , -1 , -1 ,1 , -1 ,1 ,0]
challenging = [0 , -1 ,1 , -1 , -1 ,1 , -1 , -1 ,1 , -1 ,1 , -1 , -1 ,0]
hardmode = [0 , -1 ,1 , -1 , -1 ,1 , -1 , -1 ,1 , -1 ,1 , -1 , -1 ,1 ,1 ,1 , -1 , -1 ,0]
very_hard = [0 , -1 ,1 , -1 , -1 ,1 , -1 , -1 ,1 , -1 ,1 , -1 , -1 ,1 ,1 ,1 ,
-1 ,1 , -1 , -1 ,1 , -1 ,1 , -1 , -1 ,1 , -1 , -1 ,1 , -1 ,1 ,
-1 ,1 , -1 ,1 , -1 , -1 ,1 , -1 , -1 ,1 , -1 ,1 , -1 , -1 ,0]
print (maximumScoreFrom(easy, 0))
print (maximumScoreFrom(medium, 0))
print (maximumScoreFrom(challenging, 0))
print (maximumScoreFrom(hardmode, 0))
print (maximumScoreFrom(very_hard, 0))


