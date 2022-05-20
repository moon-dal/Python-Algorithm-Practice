def quick(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, right = [], []

    for i in arr[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    left = quick(left)
    right = quick(right)
    return right + [pivot] + left



N = list(map(int, input()))
res = quick(N)
for i in res:
    print(i, end='')