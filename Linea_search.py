def linear_search(lst, target):

    """
    This function performs a linear search on the given list to find the target element.
    returns the index position  of the target if found, otherwise returns None.
    """

    for i in range(0,len(lst)):
        if lst[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the list.")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 5)
verify(result)