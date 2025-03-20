program project1124;

const N=16;
type Tarray=array[1..N] of integer;
function Scal(var X, Y:Tarray; I, J:integer):integer;
var k: integer;
begin
  Scal:=0;
  for k:=I to J do
  Scal:= Scal + X[k]*Y[k];
end;
var w, q: integer;
    X, Y:Tarray;
begin
  for w:= 1 to N do
  begin
    read(q);
    X[w]:= q;
  end;

  for w:= 1 to N do
  begin
    read(q);
    Y[w]:= q;
  end;

  if Scal(X, Y, 1, 3 * (n div 4)) > 0 then
  writeln(Scal(X, X, 1, n)) else writeln(Scal(Y, Y, (n div 2), n));
end.

