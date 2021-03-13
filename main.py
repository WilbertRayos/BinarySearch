def binary_search(value_list: list, value_search: int):
    # Get list size
    list_size = len(value_list)
    # Lowest index in the list [Initial]
    index_low = 0
    # Highest index in the list [Initial]
    index_high = list_size - 1

    # Will be used as validator if value exists
    value_found = False

    # While lowest index does not exceed highest index
    while index_low <= index_high:
        # Find the middle index of the list
        # Add the lowest index and highest index, then floor divide into 2
        index_middle = (index_high + index_low) // 2
        # If value searching is greater than the middle index
        if value_search > value_list[index_middle]:
            # New lowest index is the higher half of the list
            index_low = index_middle + 1
        # If value searching is less than the middle index
        elif value_search < value_list[index_middle]:
            # New highest index us the highest half of the list
            index_high = index_middle -1
        # If value found
        elif value_search == value_list[index_middle]:
            # Change value of value_found
            value_found = f"Value found at index {index_middle}"
            # Stops the loop
            break

    # Check if value exists
    # If value exists, display the text and index
    # If value does not exists, display value not found
    print("Value not found" if value_found == False else value_found)


binary_search([1,2,3,4,6,7,8], 8)
