from antlr4 import InputStream, CommonTokenStream
from CalcLexer  import CalcLexer
from CalcParser import CalcParser
from EvalVisitor import EvalVisitor

def calcular(expresion: str):
    # 1. Convertir el texto en un flujo de caracteres
    entrada = InputStream(expresion)

    # 2. El Lexer convierte los caracteres en tokens
    lexer  = CalcLexer(entrada)
    tokens = CommonTokenStream(lexer)

    # 3. El Parser construye el árbol sintáctico
    parser = CalcParser(tokens)
    arbol  = parser.prog()        # prog() es la regla de inicio

    # 4. El Visitor recorre el árbol y evalúa la expresión
    visitor   = EvalVisitor()
    resultado = visitor.visit(arbol)

    return resultado


# ── Punto de entrada del programa ──────────────────────
if __name__ == '__main__':
    print("=== Calculadora ANTLR4 ===")
    print("Escribe 'salir' para terminar\n")

    while True:
        try:
            expr = input("> ").strip()
            if expr.lower() == 'salir':
                break
            resultado = calcular(expr)
            print(f"= {resultado}\n")
        except Exception as e:
            print(f"Error: {e}\n")
