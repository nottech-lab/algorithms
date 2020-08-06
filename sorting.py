#Sorting in algorithm 

def quick_sort(sequence):

    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()  #removes and returns last value from the list
    items_greater = []
    items_lower = []
    
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

    print(quick_sort([4,5,2,3,0,12,34,8,8,9,45]))

