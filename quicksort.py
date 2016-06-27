
# Podstawowa wersja algorytmu
def quicksort(elements):

    # jesli ciag zawiera co najwyzej 1 element
    if len(elements) < 2:
        return elements

    else:
        # pivot - element do porownan
        pivot = elements[0]
        smaller = [x for x in elements[1:] if x < pivot]
        greater = [x for x in elements[1:] if x >= pivot]

        smaller_result = quicksort(smaller)
        greater_result = quicksort(greater)

        return smaller_result + [pivot] + greater_result
