def binary_search(arr, target):
    mid = len(arr)//2

    if arr[mid] > target:
        binary_search(arr[:mid], target)

    elif arr[mid] < target:
        binary_search(arr[mid+1:], target)

    elif arr[mid] == target:
        print(f'target {target} index is {mid}')


if __name__ == '__main__':
    # binary search는 이미 오름차순 정렬 되어있는 배열에 대해서 target 인덱스 찾는 것이므로 sort해줘야함.
    print('enter array... ex) 4 2 9 1 8')
    arr = [int(x) for x in input().split()]
    arr.sort()
    print(arr)

    print('enter target')
    target = int(input())
    print(target)

    result = binary_search(arr, target)
    print(result)