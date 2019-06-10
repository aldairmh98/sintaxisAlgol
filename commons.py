def searchWord(cad, word):
    wordSize = len(word)
    for idx in range(0, len(cad)):
        if cad[idx:idx+wordSize] == word:
            return idx
    return -1

def deleteWhiteSpaces(originalCad):
    newCad = ''
    for c in originalCad:
        if c != ' ':
            newCad += c
    return newCad

def hasParetessis(cad):
    number = 0
    for c in cad:
        if c == '(':
            number+=1
    return number
def validateParentessis(cad):
    openedP = closedP = 0
    for idx,character in enumerate(cad):
        if character == '(':
            openedP+=1
        if character == ')':
            closedP+=1
    return closedP == openedP