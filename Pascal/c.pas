program Ajuda;

var
  a, b, c, soma, total: integer;

begin
  readln(a, b, c);

  readln(soma);

  total := a + b + c;

  if total = soma then
    writeln('Acertou')
  else
    writeln('Errou');
end.
