
''' izracunati sumu elemenata liste '''
def sum(list):
    if len(list) == 0:
        return 0
    return list[0] + sum(list[1:])

# lista = [2,2,1,3,3]
# print(sum(lista))

''' rekurzivnu funkciju koja stampa prvih 50 prirodnih brojeva '''
def first_fifty(num):
    print(num)
    if num == 0:
        return num
    else:
        return first_fifty(num - 1)

# first_fifty(50)

''' Napisati rekurzivnu funkciju koja vraca najveci element liste '''
def najveci_el(list):
    if len(list) == 0:
        return 0
    else:
        max = najveci_el(list[1:])
        return max if max > list[0] else list[0]

''' rekurzivna funkcija koja stampa sve elemente liste '''
def print_list(list):
    if len(list) == 0:
        return 0
    else:
        print(list[0])
        return print_list(list[1:])

# print_list([2,4,6,1,7])


''' rekurzivna funkcija koja racua sumu cifara unijetog broja '''
def sum_digits(n):
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits(n // 10) + last_digit

# print(sum_digits(552))

''' rekurzivna funkcija koja provjerava je li string palindrom '''
def is_palindrome(str):
  if len(str) < 2:
    return True
  if str[0] != str[-1]:
    return False
  return is_palindrome(str[1:-1])

''' rekurzivna funkcija fibbonacijev niz'''
def fibonacci(n):
  if n < 0:
    raise ValueError("Input 0 or greater only!")
  fiblist = [0, 1]
  for i in range(2,n+1):
    fiblist.append(fiblist[i-1] + fiblist[i-2])
  return fiblist[n]


''' rekurzivna funkcija za racunanje faktorijela '''
def factorial(n):
  answer = 1
  while n != 0:
    answer *= n
    n -= 1
  return answer

''' rekurzivna funkcija za pronalazenje najmanjeg elementa u listi '''
def find_min(my_list):
  if len(my_list) == 0:
    return None
  if len(my_list) == 1:
    return my_list[0]
  #compare the first 2 elements
  temp = my_list[0] if my_list[0] < my_list[1] else my_list[1]
  my_list[1] = temp
  return find_min(my_list[1:])

# print(find_min([]) == None)
# print(find_min([42, 17, 2, -1, 67]) == -1)

