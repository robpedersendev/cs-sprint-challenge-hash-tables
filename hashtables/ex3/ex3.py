# Build a helper function to check to see if the duplicate value exists
def does_duplicate_exist(value, dicts):
    # Loop through all dictionaries
    for dict in dicts:
        # The the value provided is not in the dict
        if value not in dict:
            # Return false
            return False
    # Otherwise return True
    return True


def intersection(arrays):
    # Create the array to hold all unique values
    unique_array = []

    # Loop through the arrays
    for array in arrays:
        # Create a unique values dictionary
        one_offs = {}
        # For each individual value in the array
        for value in array:
            # For each value, set it to equal true
            one_offs[value] = True
        # Add each one_offs dictionary to the unique_array
        unique_array.append(one_offs)
    final = unique_array[-1]
    # Create a result array
    result = []

    for value in final:
        if does_duplicate_exist(value, unique_array[:-1]):
            result.append(value)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
