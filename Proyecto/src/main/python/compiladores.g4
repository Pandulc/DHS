grammar compiladores;

fragment LETRA: [A-Za-z];
fragment DIGITO: [0-9];

EQ: '=';
EQQ: '==';
NE: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
PP: '++';
MM: '--';
PA: '(';
PC: ')';
LLA: '{';
LLC: '}';
PYC: ';';
COMA: ',';

NUMERO: DIGITO+;

TDATO: 'int' | 'double';
WHILE: 'while';
IF: 'if';
FOR: 'for';
RETURN: 'return';
ID: (LETRA | '_') (LETRA | DIGITO | '_')*;
WS: [ \t\n\r] -> skip;
OTRO: .;

programa: instrucciones EOF;

instrucciones: instruccion instrucciones |;

instruccion:
	declaracion
	| retornar
	| asignacion
	| if_stmt
	| while_stmt
	| for_stmt
	| bloque;

declaracion: TDATO ID definicion lista_var;

definicion: EQ NUMERO | EQ NUMERO PYC |;

bloque: LLA instrucciones LLC;

lista_var: COMA ID definicion lista_var |;

asignacion: ID definicion;

retornar: (RETURN ID PYC) | (RETURN NUMERO PYC);

while_stmt: WHILE PA opal PC instruccion;

if_stmt: IF PA opal PC instruccion;

for_stmt:
	(
		FOR PA (asignacion | ID) PYC (
			ID opal ID
			| ID opal NUMERO
		) PYC (ID PP | ID MM | asignacion) PC instruccion
	);
opal: (ID loperators ID) | (ID loperators NUMERO);

loperators: (EQQ | GE | GT | LE | LT | NE);

//El FOR se rompe, ver que onda con eso, if anda bien, while no probe, return no lo vi, preguntar
// punto y coma que termina el for (en vez de que hayan instrucciones dentro del for, lo cierro con
// ;, como esta en el prueba.txt)