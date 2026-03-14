grammar Calc;

// ── REGLAS DEL PARSER (minúsculas) ──────────────────

prog
    : expr EOF                        // Un programa es una expresión seguida del fin de entrada
    ;

expr
    : expr op=('*' | '/') expr       // Multiplicación y división (mayor precedencia)
    | expr op=('+' | '-') expr       // Suma y resta (menor precedencia)
    | '(' expr ')'                   // Expresión entre paréntesis
    | NUM                             // Un número
    ;

// ── REGLAS DEL LEXER (MAYÚSCULAS) ───────────────────

NUM
    : [0-9]+ ('.' [0-9]+)?          // Número entero o decimal
    ;

WS
    : [ \t\r\n]+ -> skip              // Ignorar espacios en blanco
    ;
