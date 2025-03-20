program project1202;

function maxdigit(n: integer): integer;
var m : integer;
begin
  if n < 10 then maxdigit := n
  else begin
    m := maxdigit(n div 10);
    if (n mod 10) > m
        then maxdigit := (n mod 10)
        else maxdigit := m;
  end;
end;

function findMin(n: integer): integer;
var
  x, res: integer;
begin
  Read(x);
  if x = 0 then
    findMin := n
  else
  begin
    if n=0 then res := x
    else begin
      res := n;
      if maxDigit(Abs(x)) < maxDigit(Abs(n)) then
         res := x
   end;
   findMin := findMin(res)
  end;
end;

begin
  Writeln(findMin(0));
end.
