program project14121;

//#4.12(e)
var x, y, z:real;
begin
  readln(x); readln(y); readln(z);
  if (x + y > z) and (x + z > y) and (y + z > x)
     then
       if (x = y) and (y = z)
          then writeln(3)
          else
              if (x = y) or (x = z) or (z = y)
                 then writeln(2)
                 else writeln(1)
     else writeln(0);
  readln
end.








