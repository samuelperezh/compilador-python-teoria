# Analizador léxico
import ply.lex as lex  # Importamos la librería ply.lex para construir el analizador léxico.

# Definición de tokens que representan las unidades léxicas básicas que el analizador reconocerá.
tokens = ['NUMERO', 'MAS', 'MENOS', 'POR', 'DIVIDIDO', 'POTENCIA', 'PARENTESISIZQ', 'PARENTESISDER']

# Expresiones regulares para tokens simples.
# Cada expresión regular está asociada a un token específico.
t_MAS = r'\+'  # Token para el símbolo '+'
t_MENOS = r'-'  # Token para el símbolo '-'
t_POR = r'\*'  # Token para el símbolo '*'
t_DIVIDIDO = r'/'  # Token para el símbolo '/'
t_POTENCIA = r'\^'  # Token para el símbolo '^'
t_PARENTESISIZQ = r'\('  # Token para el símbolo '('
t_PARENTESISDER = r'\)'  # Token para el símbolo ')'

# Expresión regular para reconocer números enteros y de punto flotante.
# La función t_NUMERO define cómo se reconoce un número y cómo se almacena su valor.
def t_NUMERO(t):
    r'\d+(\.\d+)?'  # Expresión regular que reconoce enteros y números de punto flotante.
    t.value = float(t.value) if '.' in t.value else int(t.value)  # Convierte el valor a float si contiene un punto decimal, sino a int.
    return t

# Ignorar caracteres como espacios y saltos de línea.
t_ignore = ' \t\n'

# Manejo de errores de token.
# Esta función se llama cuando se encuentra un carácter no válido.
def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])  # Imprime un mensaje de error con el carácter no válido.
    t.lexer.skip(1)  # Salta el carácter no válido y continúa analizando.

# Construcción del analizador léxico.
lexer = lex.lex()  # Crea una instancia del analizador léxico.