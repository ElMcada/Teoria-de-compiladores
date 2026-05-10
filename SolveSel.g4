grammar SolveSel;

root: (action)* EOF;

action : expr '=' expr ';' #Ecuacion
       | 'solve' '(' ID ')' ';' #Resolver
       | 'print' expr ';' #Mostrar
       ;

expr : expr op=('*'|'/') expr #MulDiv
     | expr op=('+'|'-') expr #AddSub
     | term #Atom
     | '(' expr ')' #Parens
     ;

term : NUMBER ID #CoeffVar
     | ID #SoloVar
     | NUMBER #SoloNum
     ;

ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS     : [ \t\r\n]+ -> skip ;
