SUB D1, 48
SUB D2, 48
SUB D3, 48
mov al, 100
mul D1
mov bx, ax
mov ax, word ptr 10
mul D2
add ax, bx
add ax, word ptr D3
mov N, ax