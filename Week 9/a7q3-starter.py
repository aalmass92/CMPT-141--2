import numpy as np


######### PROVIDED FUNCTION, DO NOT MODIFY ############################################
def read_field(fname):
    '''
    Read data from a battlefield file.
    :param fname: The filename of the file containing battlefield data.
    :return: A 2D array of integers with penguin counts for each battlefield position.
    '''
    f = open(fname, 'r')
    data = []
    for row in f:
        line = [int(x) for x in row.rstrip().split(',')]
        data.append(line)
    return np.array(data)
########################################################################################


#
# TODO: Write the find_target_location function here.
#




field1 = read_field('field1.csv')
field2 = read_field('field2.csv')

#
# TODO: Test your function by calling it here using the arrays constructed by read_field().
# Consult the assignment description for expected results.
#
