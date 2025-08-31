# find an element in sorted 2d array in log(m*n) time complexity
def binary_search(xs, target):
    low = 0
    high = len(xs) - 1

    while low <= high:
        mid = (low + high) // 2
        if target > xs[mid]:
            low = mid + 1
        elif target < xs[mid]:
            high = mid - 1
        else:
            return xs[mid]
    return None


def binary_search_2d(td_list, target):
    low = 0
    high = len(td_list)

    while low <=high:
        mid = (low + high) // 2
        mid_row = td_list[mid]
        if target < mid_row[0]:
            high = mid - 1
        elif target > mid_row[-1]:
            low = mid + 1
        else: 
            return binary_search(mid_row, target)
    return None
        

l = [[1,2,3], [4,5,6], [7,8,9]]
s = binary_search_2d(l, 9)
print(s)