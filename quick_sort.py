# quick sort

def quick_sort(array, start, end):
    if start >= end:
        return array

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, 0, right - 1)
    quick_sort(array, right + 1, end)


if __name__ == '__main__':

    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(quick_sort(array, 0, len(array)-1))