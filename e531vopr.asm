INCLUDE console.inc
.STACK 4096

.DATA
T db ?

.CODE
START:  mov al, 1 
        mov ah, 0
        mov bl, 0
CONT: inchar T
      mov cl, T
      cmp cl, 43; первый равен +?
      je CONT2
      cmp cl, 45; первый равен -?
      je CONT2
      cmp cl, 48; первый меньше 0?
      jb ERRR1; отстановить
      cmp cl, 57; первый больше 9?
      ja ERRR1; остановить
      cmp cl, 32; превый пробел?
      je CONT3; вывод числа
CONT2:  add ah, 1; модернизируем
        intchar T+ah
        mov cl, T+ah
        cmp cl, 32; встретили пробел?
        je CONT3; вывод числа
        cmp cl, 48; встретили меньше 0?
        jb ERRR1; остановить
        cmp cl, 57; встретили больше 9?
        ja ERRR1; остановить
        cmp ah, 7; больше двойного слова?
        ja ERRR2; остановить
        jmp CONT2
CONT3:  cmp bl, ah
        jbe ...5
CONT4:  outchar T+bl
        add bl, 1
        jmp CONT3
ERRR1:  sl db 'Ошибка', 0
        mov eax, offset sl
        outstr eax
ERRR2:  sl1 db 'Переполн', 0
        sl2 db 'ение', 0
        mov eax, offset sl1
        mov eиx, offset sl2
        outstr eax
        outstr ebx
EXIT
END START