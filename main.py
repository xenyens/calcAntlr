

from antlr4 import InputStream, CommonTokenStream
from CalcLexer  import CalcLexer
from CalcParser import CalcParser
from EvalVisitor import EvalVisitor

def ejecutar(codigo: str):
    entrada = InputStream(codigo)
    lexer   = CalcLexer(entrada)
    tokens  = CommonTokenStream(lexer)
    parser  = CalcParser(tokens)
    arbol   = parser.prog()
    visitor = EvalVisitor()
    visitor.visit(arbol)

if __name__ == '__main__':
    print("=== Calculadora con variables ===")
    print("Termina con una línea vacía\n")

    lineas = []
    while True:
        linea = input("... " if lineas else "> ")
        if linea == "" and lineas:
            ejecutar("\n".join(lineas))
            lineas = []
        elif linea.lower() == "salir":
            break
        else:
            lineas.append(linea)
