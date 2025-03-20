cld
lea esi, S+N-M
lea edi,T
mov ecx, M
rep movsb

std
lea esi, S+N-M-1
lea edi, S+N-1
mov ecx, N-M
rep movsb

cld
lea esi, T
lea edi, S
mov ecx, M
rep movsb


