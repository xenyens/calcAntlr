# Generated from Calc.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,44,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,31,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,39,8,2,10,2,12,
        2,42,9,2,1,2,0,1,4,3,0,2,4,0,2,1,0,3,4,1,0,5,6,46,0,7,1,0,0,0,2,
        21,1,0,0,0,4,30,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,
        1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,1,1,0,0,0,13,
        14,5,9,0,0,14,15,5,1,0,0,15,16,3,4,2,0,16,17,5,2,0,0,17,22,1,0,0,
        0,18,19,3,4,2,0,19,20,5,2,0,0,20,22,1,0,0,0,21,13,1,0,0,0,21,18,
        1,0,0,0,22,3,1,0,0,0,23,24,6,2,-1,0,24,25,5,7,0,0,25,26,3,4,2,0,
        26,27,5,8,0,0,27,31,1,0,0,0,28,31,5,10,0,0,29,31,5,9,0,0,30,23,1,
        0,0,0,30,28,1,0,0,0,30,29,1,0,0,0,31,40,1,0,0,0,32,33,10,5,0,0,33,
        34,7,0,0,0,34,39,3,4,2,6,35,36,10,4,0,0,36,37,7,1,0,0,37,39,3,4,
        2,5,38,32,1,0,0,0,38,35,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,
        1,0,0,0,41,5,1,0,0,0,42,40,1,0,0,0,5,9,21,30,38,40
    ]

class CalcParser ( Parser ):

    grammarFileName = "Calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'*'", "'/'", "'+'", "'-'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "NUM", "WS" ]

    RULE_prog = 0
    RULE_instrucciones = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "instrucciones", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    VAR=9
    NUM=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CalcParser.EOF, 0)

        def instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.InstruccionesContext)
            else:
                return self.getTypedRuleContext(CalcParser.InstruccionesContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CalcParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.instrucciones()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1664) != 0)):
                    break

            self.state = 11
            self.match(CalcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_instrucciones

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignacionContext(InstruccionesContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.InstruccionesContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(CalcParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)


    class EvaluacionContext(InstruccionesContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.InstruccionesContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvaluacion" ):
                return visitor.visitEvaluacion(self)
            else:
                return visitor.visitChildren(self)



    def instrucciones(self):

        localctx = CalcParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CalcParser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(CalcParser.VAR)
                self.state = 14
                self.match(CalcParser.T__0)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(CalcParser.T__1)
                pass

            elif la_ == 2:
                localctx = CalcParser.EvaluacionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.match(CalcParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumResContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumRes" ):
                return visitor.visitSumRes(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(CalcParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(CalcParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class ParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = CalcParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 24
                self.match(CalcParser.T__6)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(CalcParser.T__7)
                pass
            elif token in [10]:
                localctx = CalcParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(CalcParser.NUM)
                pass
            elif token in [9]:
                localctx = CalcParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(CalcParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CalcParser.MulDivContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 33
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = CalcParser.SumResContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 36
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        self.expr(5)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




