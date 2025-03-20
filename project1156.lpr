program project1156;


const W=18416;
function Sum_of_divisors(K:integer):longint;
var i: integer;
begin
    Sum_of_divisors:=0;
    for i:=2 to trunc(sqrt(k)) do begin
    if (k mod i = 0) and (k div i <> i) then
    Sum_of_divisors:= (Sum_of_divisors + i) + (k div i);
    if (k mod i = 0) and (k div i = i) then
    Sum_of_divisors:= (Sum_of_divisors + i); end;
    Sum_of_divisors:= (Sum_of_divisors + 1);
end;
var n, i, j: integer;
  lst: array[2..W] of longint;
begin
  read(n);
  if n < 2 then begin write('Error'); exit; end;
  for i:=2 to n do
  lst[i]:= Sum_of_divisors(i);
  for i:=2 to n do
  if (lst[lst[i]] = i) and (lst[i] > i) then
  write(i, ' ', lst[i], ' ')  ;
  readln
end.
