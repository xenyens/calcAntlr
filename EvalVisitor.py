from CalcVisitor import CalcVisitor

class EvalVisitor(CalcVisitor):

    def __init__(self):
        self.variables = {}      # ← la "memoria" del intérprete

    def visitProg(self, ctx):
        resultado = None
        for instruccion in ctx.instrucciones():  # recorre cada sentencia
            resultado = self.visit(instruccion)  # evalúa la sentencia
        return resultado

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()       # obtiene el nombre "a"
        valor  = self.visit(ctx.expr())   # evalúa el lado derecho
        self.variables[nombre] = valor    # guarda en memoria
        print(f"{nombre} = {valor}")
        return valor

    def visitEvaluacion(self, ctx):
        resultado = self.visit(ctx.expr())
        print(f"= {resultado}")
        return resultado

    # ── los de antes, sin cambios ──────────────────────

    def visitMulDiv(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        if ctx.op.text == '*': return izq * der
        if ctx.op.text == '/':
            if der == 0: raise ValueError("División entre cero")
            return izq / der

    def visitSumRes(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        if ctx.op.text == '+': return izq + der
        if ctx.op.text == '-': return izq - der

    def visitParentesis(self, ctx):
        return self.visit(ctx.expr())

    def visitNumero(self, ctx):
        return float(ctx.NUM().getText())

    def visitVariable(self, ctx):          # ← nuevo
        nombre = ctx.ID().getText()
        if nombre not in self.variables:
            raise ValueError(f"Variable '{nombre}' no definida")
        return self.variables[nombre]
