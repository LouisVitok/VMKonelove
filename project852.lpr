program project852;

const n=4;
var i, k: integer;
  sr, ab, x, sum: real;
  lst: array [1..n] of real;
begin
   sum:=0;
   for i:=1 to n do
       begin
         readln(x);
         lst[i]:= x;
         sum:= sum + x
       end;
   sr:= sum / n;
   ab:= abs(sr - lst[1]);
   k:= 1;
   for i:= 2 to n do
       if abs(sr - lst[i]) < ab then
          begin
            k:=i;
            ab:= abs(sr - lst[i])
          end;
   writeln(k);
   readln
end.

