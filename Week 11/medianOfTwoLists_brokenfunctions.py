# CMPT 141 - Testing, Tracing, Debugging
# Topic(s): Testing
# Assignment 9 Question 3

def medianOfTwoLists(ls1, ls2):
    '''
    Given 2 lists whose elements are in increasing order,
    merge them into one list of elements in increasing order,
    and return the median of the merged list, which is also
    the median of the two input lists.
    :param ls1: a list in increasing order
    :param ls2: a list in increasing order
    :return: the median of the two input lists
    '''
    merged = []
    index1 = 1
    index2 = 1

    while index1 < len(ls1) and index2 < len(ls2):
        # step through the lists one element at a time
        # put the smaller element in the result
        if ls1[index1] < ls2[index2]:
            merged.append(ls2[index2])
            index1 = index1 + 1
        else:
            merged.append(ls2[index2])
            index2 = index2 + 1

    # add the remaining elements
    if index1 < len(ls1):
        merged.extend(ls1[index1:])

    # find the median
    if len(merged) == 0:
        return "The median is undefined for empty lists!"
    else:
        return merged[len(merged) // 2]
