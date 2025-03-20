SUM MACRO X
    LOCAL E
    LOCAL FL
    PUSH ECX 
    E = 1
    FL = 0
    MOV EAX, 0  
    FOR R, <X>
        IFNB <R>
            IF TYPE(R) EQ  DWORD   
                MOV ECX, R  
            ELSE 
                MOVZX ECX, R 
            ENDIF
	    IF FL EQ 1
            REPEAT E
                ADD EAX, ECX 
            ENDM  
	    ELSE
		ADD EAX, ECX 
	    ENDIF
        ENDIF 
        E = E + 1
        FL = 1 - FL
    ENDM 
    POP ECX 
ENDM