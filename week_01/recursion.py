# 1. Napisati rekurzivnu funkciju koja stampa prvih 50 prirodnih brojeva 2
"""
# def first_50(x = 1):
#     if x > 50:
#         return
#     else:
#         print(x)
#         return first_50(x+1)
# first_50()
"""

# 2. Napisati rekurzivnu funkciju koja stampa prvih n prirodnih brojeva
"""
def first_n(n):
    if n < 1:

        return 0
    else:
        print(n)
        return first_n(n-1)
first_n(30)
"""

# 3. Napisati rekurzivnu funkcija koja racuna faktorijel broja n. Oznaka za faktorijel je n!, a vazi da vrijednost dobija tako sto mnoze svi brojevi
# medjusobno, zakljucno sa n, umanjujuci ih u svakom koraku za 1, do 0. Primjer: 5! = 5 * 4 * 3 * 2 * 1 (ili 1 * 2 * 3 * 4 * 5)

"""
def fakt(n):
    if n == 0:
        return 1
    else:
        return n * fakt(n-1)

print(fakt(1))
"""

# 4. . Napisati rekurzivnu funkciju koja stampa sve elemente liste
"""
def print_list(list):
    if len(list) == 1:
        return list[0]
    else:
        print(list[0])
        return print_list(list[1:])

list = [2,5,7,1,3]
print_list(list)
"""

# 5. Napisati rekurzivnu funkciju koja prebrojava broj cifara zadatog broja.
""" 
def cif_num(num):

    if num == 0:
        return 0
    else:
        return 1 + cif_num(num // 10)
print(cif_num(32426))
"""

# 6. Napisati rekurzivnu funkciju koja vraca najveci element liste
def najveci_el(list):
    if len(list) == 1:
        return list[0]
    else:


