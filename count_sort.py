# count sort

def count_sort(array):
    count = [0] * (max(array) + 1)
    result = []

    for i in array:
        count[i] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)

    return result


if __name__ == '__main__':

    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    print(count_sort(array))
