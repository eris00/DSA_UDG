from stack import Stack

''' algoritam koji provjerava da li su zagrade u unijetom stringu ispravno zatvorene  '''

def is_match(str1, str2):
    return (str1 == "(" and str2 == ")") or (str1 == "" and str2 == "]") or (str1 == "{" and str2 == "}")

