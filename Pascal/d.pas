program ConversaoDeTemperaturas;

var
  escalaOrigem, escalaDestino: char;
  temperaturaOrigem, temperaturaDestino: real;

begin
  readln(escalaOrigem);
  readln(escalaDestino);
  
  readln(temperaturaOrigem);

  if (escalaOrigem = 'C') and (escalaDestino = 'F') then
    temperaturaDestino := (temperaturaOrigem * 9 / 5) + 32
  else if (escalaOrigem = 'C') and (escalaDestino = 'K') then
    temperaturaDestino := temperaturaOrigem + 273.15
  else if (escalaOrigem = 'F') and (escalaDestino = 'C') then
    temperaturaDestino := (temperaturaOrigem - 32) * 5 / 9
  else if (escalaOrigem = 'F') and (escalaDestino = 'K') then
    temperaturaDestino := (temperaturaOrigem - 32) * 5 / 9 + 273.15
  else if (escalaOrigem = 'K') and (escalaDestino = 'C') then
    temperaturaDestino := temperaturaOrigem - 273.15
  else if (escalaOrigem = 'K') and (escalaDestino = 'F') then
    temperaturaDestino := (temperaturaOrigem - 273.15) * 9 / 5 + 32;

  writeln(temperaturaDestino:0:2);
end.
