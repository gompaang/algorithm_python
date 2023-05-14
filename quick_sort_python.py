# quick sort (python)

def quick_sort_python(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    data = array[1:]

    left = [x for x in data if x <= pivot]
    right = [x for x in data if x > pivot]

    return quick_sort_python(left) + [pivot] + quick_sort_python(right)


if __name__ == '__main__':

    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(quick_sort_python(array))
