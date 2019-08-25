import commons
import expression

VALIDSIDS = ['w', 'x', 'y']
TERMINALSYMBOLS = ['0', '1']

#Grámatica de Algol

#<S> -> <LeftPart><Expression>
#<LeftPart> -> <Identifier>:=
#<Expression> -> <Term>+<Aritmetic>, <Term>
#Expresion -> if <boolean> then <aritmetic> else <expression>
#<boolean> -> <aritmetic> < <aritmetic>
#<Aritmetic> -> <Term>+<Aritmetic>, <Term>

#<Identifier> -> W,X,Y

#this function validate begins of cadena
def leftPartValidation(cad):
    return len(cad)>=4 and VALIDSIDS.__contains__(cad[0]) and cad[1:3] == ':='


def main():
    print('Ingrese cadena a validar:')
    cadena = input()
    cadena = commons.deleteWhiteSpaces(cadena)
    first = leftPartValidation(cadena) 
    if first:
        rightPart = cadena[3:len(cadena)]
        if expression.expressionValidation(rightPart) :
            print('Es válida')
        else:
            print('Inválida')
        return
    parentessisNumber= commons.hasParetessis(cadena)
    print(parentessisNumber)
    print('Error no se ha utilizado la parte izquierda necesaria para el lenguaje.')

if __name__ == "__main__":
    while True:
        main()
        