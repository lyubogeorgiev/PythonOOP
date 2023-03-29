def choice_pattern():
    pattern = input("Choose type of pattern:\nTriangle\nRhombus\nSquare\nPattern choice:")
    size_of_pattern = int(input("Enter pattern size: "))

    return pattern, size_of_pattern


# size = int(input())

def get_pattern_data(*data):
    print(data)
    # pattern, size = data
    # for x in range(size):
    #     space_data = size - x - 1
    #     stars_data = x + 1


get_pattern_data(choice_pattern())
