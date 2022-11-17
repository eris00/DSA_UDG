
def linear_search(data, target):
    count = 0
    for element in data:
        count += 1
        print(count)
        if element == target:
            return True
    return False

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    count = 0
    while low <= high:
        count += 1
        print(count)
        mid = (low+high) // 2
        if target == data[mid]:
            return data[mid]
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

i = 0
while i <= 100000:
    print(i, end=',')
    i += 1
