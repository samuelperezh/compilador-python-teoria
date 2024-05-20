from src.calclex import lexer  # Importamos el analizador léxico desde calclex.py.
from src.calcparse import parser  # Importamos el analizador sintáctico desde calcparse.py.

# Ruta del archivo de entrada.
input_file_path = 'input/compile.txt'
# Ruta del archivo de salida.
output_file_path = 'output/compiled.txt'

# Leer las expresiones del archivo de entrada.
with open(input_file_path, 'r') as file:
    data_list = file.readlines()  # Leemos todas las líneas del archivo y las guardamos en una lista.

# Función para redirigir la salida de error semántico a un archivo.
import sys
import io

class CaptureOutput:
    def __enter__(self):
        self.new_out = io.StringIO()  # Creamos un objeto StringIO para capturar la salida.
        self.old_out = sys.stdout  # Guardamos la salida estándar actual.
        sys.stdout = self.new_out  # Redirigimos la salida estándar al objeto StringIO.
        return self.new_out

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.old_out  # Restauramos la salida estándar original.

# Abrir el archivo de salida.
with open(output_file_path, 'w') as outfile:
    # Procesar cada expresión.
    for data in data_list:
        data = data.strip()  # Eliminar espacios en blanco y saltos de línea al inicio y al final.
        if data:  # Asegurarse de que la línea no esté vacía.
            lexer.input(data)  # Alimentar la expresión al analizador léxico.

            # Obtener los tokens reconocidos.
            outfile.write(f"Tokens para la expresión: {data}\n")
            while True:
                token = lexer.token()  # Obtener el siguiente token.
                if not token:
                    break
                outfile.write(f"{token}\n")  # Escribir el token en el archivo de salida.

            # Análisis sintáctico y semántico.
            outfile.write("Resultado del análisis:\n")
            with CaptureOutput() as captured_output:
                result = parser.parse(data)  # Analizar la expresión.
            errors = captured_output.getvalue()  # Obtener cualquier error capturado.

            # Escribir el resultado y los errores en el archivo de salida.
            if errors:
                outfile.write(errors)
            outfile.write(f"{result}\n\n")  # Escribir el resultado en el archivo de salida.