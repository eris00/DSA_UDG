from stack import Stack

''' algoritam koji provjerava da li su zagrade u unijetom stringu ispravno zatvorene  '''

def is_match(str1, str2):
    return (str1 == "(" and str2 == ")") or (str1 == "[" and str2 == "]") or (str1 == "{" and str2 == "}")

def is_parentesis_balanced(str):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(str) and is_balanced:
        parethesis = str[index]
        if parethesis in "{[(":
            s.push(parethesis)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, parethesis):
                    is_balanced = False
        index = index + 1
    return s.is_empty() and is_balanced




print(is_parentesis_balanced("([])"))