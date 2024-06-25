program SomaN;

var
  N, i, X: integer;
  soma: double;

begin
  soma := 0;

  readln(N);

  for i := 1 to N do
  begin
    readln(X);
    soma := soma + X;
  end;

  writeln(trunc(soma));
end.
