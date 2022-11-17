
''' Linearno trazenje - obicna pretraga '''
def linear_search(data, target):
    for element in data:
        if element == target:
            return True
    return False

# print(linear_search([1,4,2,5,6,8,3], 4))

''' Binarno trazenje - dijeljenje niza '''
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    count = 0
    while low <= high:
        count += 1
        print(count)
        mid = (low+high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

def recursive_binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            recursive_binary_search(data, target, low, mid-1)
        else:
            recursive_binary_search(data, target, mid+1, high)



array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# binary_search(array, 8692)

recursive_binary_search(array, 7, 0, len(array)-1)