from CalcVisitor import CalcVisitor

class EvalVisitor(CalcVisitor):

    # Visita la regla: prog : expr EOF
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    # Visita la regla: expr op=('*'|'/') expr
    def visitExpr(self, ctx):

        # Caso 2: expresión entre paréntesis → '(' expr ')'
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expr(0))

        # Caso 1: expresión con dos operandos (suma, resta, mult, div)
        if ctx.getChildCount() == 3:
            izq = self.visit(ctx.expr(0))   # Evalúa el lado izquierdo
            der = self.visit(ctx.expr(1))   # Evalúa el lado derecho
            operador = ctx.op.text          # Obtiene el operador (+, -, *, /)

            if operador == '+':
                return izq + der
            elif operador == '-':
                return izq - der
            elif operador == '*':
                return izq * der
            elif operador == '/':
                if der == 0:
                    raise ValueError("Error: División entre cero")
                return izq / der



        # Caso 3: solo un número → NUM
        elif ctx.getChildCount() == 1:
            return float(ctx.NUM().getText())

        return 0
