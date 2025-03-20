program project1021;

var k, y, p, h1, v1: char; r:'a'..'h';  v:'1'..'8';
begin
     read(r);
     read(v);
     h1:=r;
     v1:=v;
     for y:='8' downto '1' do begin
     for k:='a' to 'h' do
     if ((ord(k) = ord(r)) or (ord(y) = ord(v)) or (abs(ord(k) - ord(h1)) = abs(ord(y) - ord(v1)))) and (abs(ord(k) - ord(h1)) + abs(ord(y) - ord(v1)) <> 0) then
     write('*')
     else write('0');
     writeln; end;
     write(333);  readln(p);
end.

