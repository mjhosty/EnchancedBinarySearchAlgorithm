import names


def standardbinarysearch(array, element: str) -> list:
    e_len = len(element)
    result = []
    first = 0
    last = len(array) - 1
    mid = (first + last) // 2
    while first < last:
        if element < array[mid][:e_len]:
            last = mid - 1
        elif element > array[mid][:e_len]:
            first = mid + 1
        mid = (first + last) // 2
        if element == array[mid][:e_len]:
            result.append(array[mid])
            break
    return result


def enchancedbinarysearch(array, element: str) -> list:
    element_length = len(element)
    result = []
    first = 0
    last = len(array) - 1
    mid = (first + last) // 2
    while first <= last:
        if element < array[mid][:element_length]:
            last = mid - 1
        elif element > array[mid][:element_length]:
            first = mid + 1

        mid = (first + last) // 2

        if element == array[mid][:element_length]:
            result.append(array[mid])
            cursor_left = mid - 1
            cursor_right = mid + 1
            while cursor_left is not None or cursor_right is not None:
                if cursor_left is not None:
                    if cursor_left < 0 or element != array[cursor_left][:element_length]:
                        cursor_left = None
                    else:
                        result.append(array[cursor_left])
                        cursor_left -= 1

                if cursor_right is not None:
                    if cursor_right == len(array) or element != array[cursor_right][:element_length]:
                        cursor_right = None
                    else:
                        result.append(array[cursor_right])
                        cursor_right += 1
            break

    result.sort()
    return result




