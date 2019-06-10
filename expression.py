import commons
from booleanExpression import validateBooleanExpression
from aritmeticExpression import aritmeticValidation
from termExpression import termValidation

VALIDSIDS = ['w', 'x', 'y']
TERMINALSYMBOLS = ['0', '1']

def searchCloseParentesis(cad):
    limit = len(cad)
    myidx = limit 
    for c in cad:
        myidx-= 1
        if cad[myidx] == ')':
            return myidx
    return -1

def expressionValidation(cad):
    isAssignation = VALIDSIDS.__contains__(cad[0]) or TERMINALSYMBOLS.__contains__(cad[0])
    cadSize = len(cad)
    if (cadSize > 1):
        if isAssignation and cad[1] == '+' and cadSize>2:
            return aritmeticValidation(cad[2: cadSize])
        else:
            try:
                if cad[0:2]== 'if':
                    return validateBooleanExpression(cad)
                elif cad[0] == '(':
                    if cad[cadSize-1] == ')':
                        
                        return expressionValidation(cad[1: cadSize-1])
                    else:
                        idx = searchCloseParentesis(cad) 
                        if idx > -1 and cad[idx+1] == '+':
                            if idx+2 == cadSize-1:
                                return termValidation(cad[1:idx]) and aritmeticValidation(cad[idx+2])
                            else:
                                print(cad[idx+2, cadSize-1])
                                return False
                        else:
                            return False

            except:
                return False
            return False
    else:
        return isAssignation

