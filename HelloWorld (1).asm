mov eax, T
mov bx, word ptr 3600
div bx
mov H, al
mov bl, 60
xchg ax, dx
div bl
mov M, al
mov S, ah