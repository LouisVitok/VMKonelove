program project844;

const n=4;
var x, y: array[1..n] of char; ag:boolean; e, q,i, j, k:integer; w:char;
begin
  for i:=1 to n do
      begin
           read(w);
           x[i]:=w
      end;
  readln;
  for i:=1 to n do
      begin
           read(w);
           y[i]:=w
      end;
  readln;
  if x=y then
     begin
       writeln(false);
       exit
     end;
  ag:= true;
  for i:=1 to n do
  begin
    w:= x[i];
    k:=0;
    for j:=1 to n do
        if x[j] = w then
           k:=k+1;
    e:=0;
    for q:=1 to n do
        begin
             if y[q] = w then
                e:=e+1;
        end;
    if k<>e then
       begin
         ag:=false; break
       end;
  end;
  writeln(ag);
  readln
end.

