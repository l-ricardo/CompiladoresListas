program Ajuda;

var
  numPessoas, i, somaContas, somaCalculada, valorConta: integer;

begin
  readln(numPessoas);

  somaContas := 0;

  for i := 1 to numPessoas do
  begin
    read(valorConta);
    somaContas := somaContas + valorConta;
  end;

  readln(somaCalculada);

  if somaContas = somaCalculada then
    writeln('Acertou')
  else
    writeln('Errou');
end.
