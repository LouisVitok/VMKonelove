;Головной модуль

INCLUDE settings.inc
INCLUDE io2021.inc


EXTERN P1@0: PROC; 
 
.STACK 4096
.DATA 
	X DD ?
	Y DD ?
.CODE
start:
     ININT X
     LEA EAX, X
     PUSH EAX
     ININT Y
     MOVSX EAX, Y
     PUSH EAX
     CALL P1@0;
     OUTU X
     NEWLINE
     OUTU EAX
     NEWLINE
    EXIT
end start
