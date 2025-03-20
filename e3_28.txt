mov dx, word ptr T+2
mov ax, word ptr T
mov bx, 60
div bx
mov S, dl
mov dh, 0
mov bl, 60
div bl
mov M, ah
mov H, al