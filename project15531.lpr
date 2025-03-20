program project15531;

const n=4;
var cur, pr, i: integer;

begin
  readln(pr);
  pr:=abs(pr);
  for i:=1 to n-1 do
  begin
    readln(cur);
    cur:=abs(cur);
    while pr<>cur do
          if pr>cur then
          pr:=pr - cur
          else cur:=cur - pr
  end;
  writeln(pr);
  readln
end.
