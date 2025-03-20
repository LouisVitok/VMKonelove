program project1438;

var lst: array[1..21] of boolean; i: integer; x: char; fl, fl2: boolean; w: set of char; lst2:array[1..21] of char;
begin
   lst2[1]:= 'b';
   lst2[2]:= 'c';
   lst2[3]:= 'd';
   lst2[4]:= 'f';
   lst2[5]:= 'g';
   lst2[6]:= 'h';
   lst2[7]:= 'j';
   lst2[8]:= 'k';
   lst2[9]:= 'l';
   lst2[10]:= 'm';
   lst2[11]:= 'n';
   lst2[12]:= 'p';
   lst2[13]:= 'q';
   lst2[14]:= 'r';
   lst2[15]:= 's';
   lst2[16]:= 't';
   lst2[17]:= 'v';
   lst2[18]:= 'w';
   lst2[19]:= 'x';
   lst2[20]:= 'y';
   lst2[21]:= 'z';
   w:= ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'];
   fl:=false;
   for i:=1 to 21 do
   lst[i]:=false;
   fl2:=false;
   repeat
     read(x);
     if not fl then
     if x<>'.' then
     fl:=true;
     if ((ord(x) < 97) or (ord(x) > 122)) and (ord(x) <> 32) and (ord(x) <> 46) and (ord(x) <> 44) then begin write('Error'); exit; end;
     if not fl2 then
     if (x=',') or (x='.') then begin write('Error'); exit; end;
     if not fl2 then
     if x<>',' then fl2:=true;
     if fl2 then
     if x=',' then fl2:=false;
     if x = 'b' then lst[1]:=true;
     if x = 'c' then lst[2]:=true;
     if x = 'd' then lst[3]:=true;
     if x = 'f' then lst[4]:=true;
     if x = 'g' then lst[5]:=true;
     if x = 'h' then lst[6]:=true;
     if x = 'j' then lst[7]:=true;
     if x = 'k' then lst[8]:=true;
     if x = 'l' then lst[9]:=true;
     if x = 'm' then lst[10]:=true;
     if x = 'n' then lst[11]:=true;
     if x = 'p' then lst[12]:=true;
     if x = 'q' then lst[13]:=true;
     if x = 'r' then lst[14]:=true;
     if x = 's' then lst[15]:=true;
     if x = 't' then lst[16]:=true;
     if x = 'v' then lst[17]:=true;
     if x = 'w' then lst[18]:=true;
     if x = 'x' then lst[19]:=true;
     if x = 'y' then lst[20]:=true;
     if x = 'z' then lst[21]:=true;
   until x = '.';
   if not fl then begin write('Error'); exit; end;
   for i:=1 to 21 do
   if lst[i]=false then write(lst2[i]);
end.

