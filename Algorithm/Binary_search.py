def binary_search(list, goal):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = int((start + end) / 2)
        guess = list[mid]
        if guess == goal:
            return mid
        elif guess > goal:
            end = mid - 1
        else:
            start = mid + 1
    return None

my_list = [1, 3, 5, 7, 9, 19]
other_list = [3, 5, 7, 12, 23]
print(binary_search(my_list, 9))
print('index of goal:', binary_search(other_list, 5))