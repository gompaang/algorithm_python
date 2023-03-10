def quick_sort(input, start, end):
    if start >= end:
        return input

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and input[left] <= input[pivot]:
            left += 1
        while right > start and input[right] >= input[pivot]:
            right -= 1

        if left > right:
            input[right], input[pivot] = input[pivot], input[right]
        else:
            input[left], input[right] = input[right], input[left]

    quick_sort(input, 0, right - 1)
    quick_sort(input, right + 1, end)


if __name__ == '__main__':
    print('enter array... ex) 4 2 9 1 8')
    arr = [int(x) for x in input().split()]
    print(arr)

    quick_sort(arr, 0, len(arr)-1)
    print(arr)