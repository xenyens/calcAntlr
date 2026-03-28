from CalcVisitor import CalcVisitor

class EvalVisitor(CalcVisitor):

    # Visita la regla: prog : expr EOF
    def visitProg(self, ctx):
        return self.visit(ctx.expr())


    def visitSumRes(self, ctx):
        print("visitSumRes")
        left = self.visit(ctx.expr(0))  # Primer operando
        right = self.visit(ctx.expr(1)) # Segundo operando

        if ctx.op.text == '+':
            return left + right

        return left - right



    # Visit a parse tree produced by CalcParser#Numero.
    def visitNumero(self, ctx):
        return float(ctx.NUM().getText())


