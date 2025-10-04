def binary_search(list, target):
    fist = 0
    last = len(list) - 1

    while fist <= last:
        midpoint = (fist + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            fist = midpoint + 1
        else:
            last = midpoint - 1
    return None    

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the list.")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 5)
verify(result)