def find_smallest(arr):
    smallest = arr[0]
    arr_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            arr_index = i
    return arr_index

# print(find_smallest([1, 6, 2, 13]))

def selectionsort(arr):
    newArr = []
    while len(arr):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest)) #删除列表中给定位置的元素并返回它
    return newArr

print(selectionsort([6, 7, 2, 9, 4]))

