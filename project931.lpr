program project931;

const n=4;
var A: array[1..n, 1..n] of integer;
  i, j, sum, x, k: integer;
begin
  sum:= 0;
  for i:=1 to n do
  for j:=1 to n do
      begin
        read(x);
        A[i,j]:= x
      end;
  for j:=1 to n do
      sum:= sum + A[1, j];

  for i:=2 to n do
    begin
      k:=0;
      for j:=1 to n do
      k:= k + A[i, j];
      if k <> sum then
      begin
           writeln(false);
           exit
      end;
    end;

   for j:=1 to n do
    begin
      k:=0;
      for i:=1 to n do
      k:= k + A[i, j];
      if k <> sum then
      begin
           writeln(false);
           exit
      end;
    end;
   writeln(true);
   readln
end.

