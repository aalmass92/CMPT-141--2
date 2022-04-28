# list for fruits abbreviation
fruit_List = ['F', 'W', 'G', 'J', 'M']
# list of fruits full names and their indexes
# in the list of abbreviation to match order in sample output
tree_List = [('Waterfruits', 1), ('Grassfruits', 2), ('Megafriuts', 4), ('Firefruits', 0), ('Joltfruits', 3)]


def create_farm(file):
    """ Read file and create initial garden.

    :param file: name of file to read (str)
    :return: list of list of strings
    """
    # open file

    try:
        with open(file) as f:
        # read first line and convert into integer
        # read other lines
            try:
                trees_number = int(f.readline())
                trees = [line.strip() for line in f.readlines()[:trees_number]]
        # if file has invalid format
        # return empty list
            except (ValueError, IndexError):
                return []
            # create initial state (garden)
            garden = create_state(trees_number, trees)
                return garden
        # if file does not exist
        # return empty list
        except (FileExistsError, FileNotFoundError):
            return []

