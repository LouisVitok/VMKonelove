program project918;

const n=3;
  m=3;
var A: array[1..n, 1..m] of integer;
  b: array[1..n] of boolean;
  i, j, x:integer;
begin
  for i:=1 to n do
  for j:=1 to m do
  begin
    readln(x);
    A[i, j]:= x
  end;
  for i:=1 to n do
  b[i]:= true;
  for i:=1 to n do
  for j:=2 to m do
      if A[i][j - 1] <= A[i][j] then
      begin
        b[i]:= false;
        break
      end;
for i:=1 to n do
writeln(b[i]);
readln
end.

