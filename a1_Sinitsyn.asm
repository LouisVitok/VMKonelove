; Вспомогательный модуль

INCLUDE settings.inc
 
PUBLIC P1
 
N = 1

.DATA
.CODE
P1 PROC
  	POP Y
	POP X
	MOVSX EBX, Y
	IMUL EBX
	MOVSX EAX, [X]
	IMUL EAX
	MOV [X], EBX
P1 ENDP

end