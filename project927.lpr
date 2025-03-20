program project927;

const n=4;
var A: array [1..n, 1..n] of integer;
  i, j, x: integer;
begin
  for i:=1 to n do
  for j:=1 to n do
      begin
        read(x);
        A[i, j]:= x
      end;
  for i:=1 to n-1 do
  for j:=i+1 to n do
  if A[i, j] <> A[j, i] then
  begin
    writeln(false);
    exit
  end;
  writeln(true);
  readln
end.

