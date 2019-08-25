import commons
from aritmeticExpression import aritmeticValidation
import expression
#<boolean> -> <aritmetic> < <aritmetic>
def validateBoolean(cad):
    cadSize = len(cad)
    if cadSize < 3:
        return False
    elif cadSize == 3:
        if cad[1] == '<' or cad[1] == '=':
            return aritmeticValidation(cad[0]) and aritmeticValidation(cad[2])
        else:
            return False
    else:
        aritmetics = my_split(cad)
        if len(aritmetics) < 2:
            return False
        else:
            print(aritmetics[0], aritmetics[1])
            return aritmeticValidation(aritmetics[0]) and aritmeticValidation(aritmetics[1])
    return False

#if <boolean> then <aritmetic> else <expression>
def validateBooleanExpression(cad):
    cadSize = len(cad)
    idx_then = commons.searchWord(cad[2:cadSize], 'then')+2
    if idx_then <4 or idx_then+4==cadSize:
        return False
    else:
        idx_else = commons.searchWord(cad[2:cadSize], 'else')+2
        if idx_else > -1 :
            if validateBoolean(cad[2:idx_then]):
                print(cad[idx_then+4: idx_else], )
                return aritmeticValidation(cad[idx_then+4: idx_else]) and expression.expressionValidation(cad[idx_else+4])
        else:
            print('No cuenta con la expresión else')
            return False
    return False

def my_split(cad):
    if cad.__contains__('='):
        return cad.split('=')
    elif cad.__contains__('<'):
        return cad.split('<')
    else:
        return []        
