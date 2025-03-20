program main8_57;

var A: array[32..127] of Boolean;
x: char; i: integer;
begin
  for i:=32 to 127 do
    A[i]:=false;
  read(x);
  while x <> '.' do
  begin
    if not A[ord(x)] then
    begin
    write(x);
    A[ord(x)]:=true;
    end;
    read(x);
    end;
end.
