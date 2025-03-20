program project1161;

const N=2;
type Tmatrix=array[1..N,1..N] of real;
procedure Mult(var A, B, C:Tmatrix);
var i, j, k: integer; sum: real;
begin
  for i:=1 to N do
  for j:=1 to N do
  begin
    C[i, j]:=0;
    for k:=1 to N do
    C[i, j]:= C[i, j] + A[i, k]*B[k,j];
  end;
end;
var i, j, p, st: integer; x:real; A, B, C, D, Rez, Rez1:Tmatrix;
begin
   for i:=1 to N do
   for j:=1 to N do
   begin
     read(x);
     A[i,j]:= x
   end;

   for i:=1 to N do
   for j:=1 to N do
   begin
     read(x);
     B[i,j]:= x
   end;

   for i:=1 to N do
   for j:=1 to N do
   begin
     read(x);
     C[i,j]:= x
   end;

   read(p);
   if p <= 0 then
   begin
     write('Error'); exit;
   end;

   Mult(A, B, D);
   Mult(D, C, Rez);
   Rez1:= Rez; D:= Rez;
   for i:=2 to p do
   begin
     Mult(Rez1, Rez, D);Rez1:=D;
   end;

  for i:=1 to N do
  begin
   for j:=1 to N do begin
     write(D[i,j]:0:6); write('         ');
   end;
   writeln();
  end;
  readln(st);
end.