def binsearch_iterative(sequence, element):
    section_begin = 0
    section_end = len(sequence) - 1
    while section_begin <= section_end:
        middle_index = section_begin + section_end / 2

        if sequence[section_end] < element or sequence[section_begin] > element:
            return -1

        if sequence[middle_index] == element:
            # znalezlismy nasza zgube! :)
            return middle_index

        elif sequence[middle_index] < element:
            section_begin = middle_index + 1

        else:
            section_end = middle_index - 1

    # nie znalezlismy niczego
    return -1


def binsearch_recursive(sequence, element, section_begin=None, section_end=None):
    if section_end is None:
        section_end = len(sequence) - 1

    if section_begin is None:
        section_begin = 0

    if sequence[section_end] < element or sequence[section_begin] > element:
        return -1

    middle_index = section_begin + section_end / 2

    if sequence[middle_index] == element:
        return middle_index

    elif sequence[middle_index] < element:
        return binsearch_recursive(sequence, element, middle_index + 1, section_end)

    else:
        return binsearch_recursive(sequence, element, section_begin, middle_index - 1)

