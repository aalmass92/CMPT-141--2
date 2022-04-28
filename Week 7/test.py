# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547
#Covid Data Analysis


def read_pokedata(file):
    """
        Function reads pokemonTypes format text files and returns PokeTypeDB dictionary-of-dictionaries
    :param file: pokemonTypes format file
    :return: PokeDB dictionary of dictionaries
    """

    f = open(file, 'r')
    # Master list of file spliting by column
    masterList = [line.rsplit(',') for line in f]
    f.close()

    # pokemon list
    pokemon = [x[0] for x in masterList]

    # pokemon Type list
    pokemonType = [x[1] for x in masterList]

    # This step is to create a list of list of location
    f = open(file, 'r')
    # Master list 2 removing \n
    masterList2 = [line.rsplit('\n') for line in f]
    f.close()

    new1 = [x[0:len(masterList2)] for x in masterList2]  # spliting list
    new2 = [x[0:len(new1)][0] for x in new1]  # creating spliting list
    new3 = [x[0:len(new1)] for x in new2]  # creating another spliting list
    new4 = [x.split(',') for x in new3]  # split lines into columns
    # new5 = [x[0].strip() for x in new4]# strip each list of columns

    locationList = [x[2:] for x in new4]  # spliting each columns with only location

    # dictionary db by using a list comparison, used expression to format db
    PokeDB = {pokemon[i]: {'name': pokemon[i], 'type': pokemonType[i], 'location': locationList[i]} for i in
              range(len(pokemon))}

    # Return Pokemon DB
    return PokeDB



def find_types(database):
    """

    :param database: Pokemon Database
    :return: return a list of pokemon Types from the database
    """

    # empty list
    pokemonTypes = []

    # iterate database, condition if type is not in the list add it
    for d1 in database:
        v = database[d1]
        vType = v['type']
        if vType not in pokemonTypes:
            pokemonTypes.append(vType)

    return pokemonTypes


def type_names(database, type):
    """

    :param database: Pokemon Database
    :param type: Specific pokemon type
    :return: return a list of pokemon names from database and only specific pokemon type given
    """

    # empty list
    pokeName = []
    # iterate database condition if type is not in the list add
    for d1 in database:
        v = database[d1]
        vType = v['type']
        if vType == type:
            pokeName.append(v['name'])
    return pokeName


def count_locations(database, pokeNames):
    """
    :param database: takes in a pokemon format database
    :param pokeNames: list of pokemon names
    :return: return dictionary of locations and count of how many pokemon
    """
    # declated empty list
    Pokelocation = []
    list = []
    flatlist = []

    # iterate through database using if statement to add location
    for d1 in database:
        v = database[d1]
        vLocation = v['location']

        if d1 in pokeNames:
            list.append(vLocation)
    # make the list of a list to regular list
    for s in list:
        for i in s:
            flatlist.append(i)
    # remove all the duplicates
    for s in flatlist:
        if s not in Pokelocation:
            Pokelocation.append(s)
    # create dic with list comparison
    Pokelocation = {x: flatlist.count(x) for x in Pokelocation}
    # return a dic
    return Pokelocation

#file
fgod= 'pokemonTypes.txt'

#pokemon db
pokemonDB = read_pokedata(fgod)
#call all types
Pokemontypes = find_types(pokemonDB)

#iterate through all the poke types

counttype = []

for poketypeNam in Pokemontypes:


    typename = type_names(pokemonDB, poketypeNam)
    location = count_locations(pokemonDB, typename)


    counttype.append(len(typename))
    print(poketypeNam+' type contains '+str(len(typename))+' pokemon.')
    print('Below are the locations, where pokemon of type '+poketypeNam +' can be caught and the number of pokemon of that specific type found on those locations.')
    print(location)



#print(counttype)
#print(Pokemontypes)

import matplotlib.pyplot as plt


plt.bar(Pokemontypes,counttype)
plt.title('Total number of pokemon of different types' )
plt.xlabel('Pokemon Types')
plt.ylabel('Number of Pokemon')
plt.show()