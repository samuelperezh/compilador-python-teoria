# Analizador sintáctico y semántico (el semántico está en las reglas de producción)
import ply.yacc as yacc  # Importamos la librería ply.yacc para construir el analizador sintáctico.
from src.calclex import tokens  # Importamos los tokens definidos en el archivo calclex.py.

# Reglas de precedencia (sintáctico) para resolver ambigüedades en las operaciones.
precedence = (
    ('left', 'MAS', 'MENOS'),  # La suma y resta tienen la misma precedencia y se asocian a la izquierda.
    ('left', 'POR', 'DIVIDIDO'),  # La multiplicación y división tienen la misma precedencia y se asocian a la izquierda.
    ('right', 'POTENCIA'),  # La potencia se asocia a la derecha.
    ('right', 'UMINUS'),  # La negación unaria (menos) se asocia a la derecha.
)

# Reglas de producción (sintáctico y semántico) que definen la gramática de las expresiones.
# Cada función define cómo se estructura y evalúa una expresión específica.
def p_expression_binop(p):
    '''expression : expression MAS expression
                  | expression MENOS expression
                  | expression POR expression
                  | expression DIVIDIDO expression
                  | expression POTENCIA expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            print("Error semántico: División por cero")
            p[0] = None
        else:
            p[0] = p[1] / p[3]
    elif p[2] == '^':
        if p[3] == 0.5 and p[1] < 0:
            print("Error semántico: Raíz cuadrada de un número negativo")
            p[0] = None
        else:
            p[0] = p[1] ** p[3]

# Regla de producción (sintáctico) para la negación unaria.
def p_expression_uminus(p):
    'expression : MENOS expression %prec UMINUS'
    p[0] = -p[2]

# Regla de producción (sintáctico) para números.
def p_expression_numero(p):
    'expression : NUMERO'
    p[0] = p[1]

# Regla de producción (sintáctico) para expresiones entre paréntesis.
def p_expression_parentheses(p):
    'expression : PARENTESISIZQ expression PARENTESISDER'
    p[0] = p[2]

# Manejo de errores de sintaxis.
def p_error(p):
    print("Error de sintaxis en la entrada:", p)

# Construcción del analizador sintáctico, simplemente crea las reglas descritas.
parser = yacc.yacc()