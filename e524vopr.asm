INCLUDE settings.inc
INCLUDE io2021.inc
.STACK 4096

.DATA
T dd ?

.CODE
START: inint T
        mov cl, 0; счетчик делителей
        mov bx, 0; делитель
CHICL: add bx, 1
        mov dx, word ptr T+2
        mov ax, word ptr T
        div bx
        cmp dx, 0; остаток ноль?
        je PROVE
        jmp CHICL 
PROVE: cmp bx, ax; целое и делитель равны?
        je PROVE1
        cmp bx, T
        je PROVE1
        add cl, 1
        jmp CHICL
PROVE1: add cl, 1
        outint cl

EXIT
END START