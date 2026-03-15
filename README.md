# 🧮 Calculadora de Expresiones con ANTLR4 + Python

Implementación de una calculadora de expresiones matemáticas usando **ANTLR4** y **Python**, como ejercicio introductorio al diseño de lenguajes con análisis semántico mediante el patrón **Visitor**.

Este proyecto es el punto de partida para el diseño de un lenguaje propio con soporte semántico.

---

## ✨ Características

- Operaciones: suma `+`, resta `-`, multiplicación `*`, división `/`
- Soporte de **paréntesis** para agrupar expresiones
- **Precedencia de operadores** resuelta por la gramática
- Números enteros y decimales
- Manejo de errores: división entre cero y expresiones inválidas
- Arquitectura limpia: **Lexer → Parser → AST → Visitor**

---

## 📁 Estructura del proyecto

```
calculadora/
├── Calc.g4              # Gramática ANTLR4
├── CalcLexer.py         # Generado por ANTLR4
├── CalcParser.py        # Generado por ANTLR4
├── CalcVisitor.py       # Generado por ANTLR4 (clase base)
├── EvalVisitor.py       # Implementación semántica (Visitor)
└── main.py              # Programa principal
```

> Los archivos `CalcLexer.py`, `CalcParser.py` y `CalcVisitor.py` se generan automáticamente. Ver sección **Instalación**.

---

## ⚙️ Requisitos

| Herramienta | Versión |
|---|---|
| Python | 3.8 o superior |
| Java (JRE) | 8 o superior |
| antlr4-python3-runtime | 4.13.2 |

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/calculadora-antlr4.git
cd calculadora-antlr4
```

### 2. Instalar el runtime de Python

```bash
pip install antlr4-python3-runtime==4.13.2
```

### 3. Descargar el JAR de ANTLR4

Descarga [`antlr-4.13.2-complete.jar`](https://www.antlr.org/download/antlr-4.13.2-complete.jar) y guárdalo en una ruta accesible.

### 4. Generar el código desde la gramática

```bash
# Windows
java -jar C:\antlr\antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor Calc.g4

# Mac / Linux
java -jar ~/antlr/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor Calc.g4
```

---

## ▶️ Uso

```bash
python main.py
```

```
=== Calculadora ANTLR4 ===
Escribe 'salir' para terminar

> 3 + 5
= 8.0

> 10 - 3 * 2
= 4.0

> (10 - 3) * 2
= 14.0

> 100 / 4 + 2.5
= 27.5

> salir
```

---

## 🏗️ Arquitectura

El proyecto sigue el pipeline clásico de un compilador/intérprete:

```
Texto de entrada
      │
      ▼
  [ LEXER ]  ─── Convierte caracteres en tokens (NUM, +, -, *, /, paréntesis)
      │
      ▼
  [ PARSER ] ─── Construye el Árbol Sintáctico (AST) aplicando la gramática
      │
      ▼
  [ VISITOR ] ── Recorre el AST y evalúa cada nodo semánticamente
      │
      ▼
   Resultado
```

### Gramática (`Calc.g4`)

Las alternativas de `expr` están ordenadas por **precedencia** (mayor a menor). ANTLR4 resuelve la ambigüedad por el orden de aparición:

```antlr
expr
    : expr op=('*'|'/') expr   # MulDiv      ← mayor precedencia
    | expr op=('+'|'-') expr   # AddSub
    | '(' expr ')'             # Parentesis
    | NUM                      # Numero      ← menor precedencia
    ;
```

### Visitor (`EvalVisitor.py`)

Cada alternativa etiquetada en la gramática genera un método `visit` propio, lo que mantiene el código limpio y extensible:

```python
def visitMulDiv(self, ctx):   # maneja * y /
def visitAddSub(self, ctx):   # maneja + y -
def visitParentesis(self, ctx): # maneja ( expr )
def visitNumero(self, ctx):   # maneja un número literal
```

---

## 🔭 Posibles extensiones

- [ ] Potenciación `^`
- [ ] Negación unaria `-5 + 3`
- [ ] Variables y asignaciones `x = 5`
- [ ] Funciones matemáticas `sqrt()`, `sin()`, `cos()`
- [ ] Modo interactivo con historial

---

## 📚 Referencias

- [Documentación oficial de ANTLR4](https://www.antlr.org/)
- [antlr4-python3-runtime en PyPI](https://pypi.org/project/antlr4-python3-runtime/)
- *The Definitive ANTLR 4 Reference* — Terence Parr

---

## 👩‍💻 Autora

**Xenia Padilla Madrid**  
Docente · TECNM - Instituto Tecnológico de Ensenada  
Materia: Lenguajes y Autómatas II

---

## 📄 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
