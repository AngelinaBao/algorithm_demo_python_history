import pysnooper
@pysnooper.snoop()
def quick_sort(data):
    if len(data) >= 2:
        mid = data[len(data) - 1]
        left, right = [], []
        data.remove(mid)
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data

t = [6, 1, 23, 12, 20]
print(quick_sort(t))
