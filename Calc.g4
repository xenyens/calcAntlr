grammar Calc;

prog : instrucciones+ EOF ;          // Un programa es una o más sentencias

instrucciones
    : VAR '=' expr ';'       # Asignacion    // a = 10;
    | expr ';'              # Evaluacion    // 20 + 4;
    ;

expr
    : expr op=('*'|'/') expr   # MulDiv
    | expr op=('+'|'-') expr   # SumRes
    | '(' expr ')'             # Parentesis
    | NUM                      # Numero
    | VAR                      # Variable     // ← nuevo
    ;

VAR : [a-zA-Z_][a-zA-Z_0-9]* ;   // nombre de variable
NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
