# Generated from Calc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete generic visitor for a parse tree produced by CalcParser.

class CalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcParser#prog.
    def visitProg(self, ctx:CalcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Asignacion.
    def visitAsignacion(self, ctx:CalcParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Evaluacion.
    def visitEvaluacion(self, ctx:CalcParser.EvaluacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#SumRes.
    def visitSumRes(self, ctx:CalcParser.SumResContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Numero.
    def visitNumero(self, ctx:CalcParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Variable.
    def visitVariable(self, ctx:CalcParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#MulDiv.
    def visitMulDiv(self, ctx:CalcParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#Parentesis.
    def visitParentesis(self, ctx:CalcParser.ParentesisContext):
        return self.visitChildren(ctx)



del CalcParser