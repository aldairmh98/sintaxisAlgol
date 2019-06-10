import expression
VALIDSIDS = ['w', 'x', 'y']
TERMINALSYMBOLS = ['0', '1']
#<Term> ->  W,X,Y,0,1
#<Term> -> (Expression)
def termValidation(cad):
    if len(cad)>1:
        if cad[0] == '(' and cad[len(cad)-1] == ')':
            return expression.expressionValidation(cad[1: len(cad)-1])
    else:
        return  VALIDSIDS.__contains__(cad[0]) or TERMINALSYMBOLS.__contains__(cad[0])