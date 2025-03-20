program project1017;

const n=50; m=40;
  var A: packed array[1..n] of string[m];
    x, q:char; i, k, j, q1, g:integer;
    fl, fl2: boolean;
begin
   fl:= true;
   i:= 1; j:=1;
   repeat
     read(x);
     if (x<>' ') and (x<>'.') then
        begin
          if not fl then
             fl:=true;
          A[i][j]:= x;
          j:= j + 1;
        end;
     if (x=' ') or (x='.') then
     begin
       for k:=j to m do
       A[i][k]:=' ';
       if fl then begin i:=i+1; fl:=false; end;
       j:=1;
     end;
   until x='.';
   if i<2 then exit;
   for k:=1 to i - 2 do
   begin
   fl2:=false ;
   for g:=1 to m do
   if A[k,g]<>' ' then
   if (A[k,g] <> A[i - 1,g]) or ((A[k,g+1]=' ') and (A[i - 1,g+1]<>' ')) then
   fl2:=true;
   if A[k][g]<>A[i - 1][g] then
   fl2:=true;
   if fl2 then
      begin
        q:=A[k][1];
        q1:=0;
        for j:=1 to m do
        begin
        if A[k][j] = q then
          begin
            q1:=q1 + 1;
          end;
         end;
        if q1 > 1 then
          begin
           for j:=1 to m do
           if A[k,j]<>' ' then
               write(A[k][j]);
           writeln
           end;
      end; readln; end;
end.

