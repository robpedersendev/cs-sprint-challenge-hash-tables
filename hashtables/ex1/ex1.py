def get_indices_of_item_weights(weights, length, limit):
    # Implement a dictionary
    dict = {}

    # For every item in "length" value loop through
    for item in range(length):
        # And set the weight value's (based off of the index) as the value
        dict[weights[item]] = item
    # Create another loop based off the input of "length"
    for item in range(length):
        # Set the target equal to limit minus the weights arrays index value
        target = limit - weights[item]
        # Showing what step the test is on
        print(f"limit: {limit} - weights[item]: {weights[item]} = target: {target} ")
        # If the target value is in fact in the dictionary
        if target in dict: # Create a tuple returning the largest number first
            # If the value at the index of the dictionary is larger then the item
            if dict[target] > item:
                # Place it first
                return dict[target], item
            # Otherwise
            else:
                # Place the items value first
                return item, dict[target]

    return None