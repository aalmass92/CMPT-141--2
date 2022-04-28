# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547
def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def permutations_inner(list_of_characters, index, final_result):

    if  index == len(list_of_characters) -1:

        #print(list_of_characters)
        final_result.append(list_of_characters)
    for i in range(index, len(list_of_characters)):
        print(final_result)
        swap(list_of_characters, index, i)
        permutations_inner(list_of_characters, index + 1, final_result)
        swap(list_of_characters, index, i)

       # print(final_result)
    
# Recursive function to generate all permutations of a string
def permutations(list_of_characters):
    final_result = []
    permutations_inner(list_of_characters, 0, final_result)
    return final_result

print (permutations(['c', 'a', 't']))
