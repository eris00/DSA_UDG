def merge_sort(arr):
    if len(arr) > 1:
        #trazenje srednjeg elementa niza (indexa)
        mid = len(arr) // 2
        L = arr[:mid]
        print(L)


arr = [38, 27, 43, 3, 9, 82, 10]

merge_sort(arr)