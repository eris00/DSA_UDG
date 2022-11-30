''' koliko u zadatoj cifri ima dvocifrenih brojeva '''

def dvocifreni(list):
    if len(list) == 0:
        return 0
    if list[1:] // 10 > 9:
        return dvocifreni(list[1:])

lista = [2,7,22,4,3,51,9]
print(dvocifreni(lista))