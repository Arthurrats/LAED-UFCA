# Letra a: a lista ficará totalmente ordenada, pois há uma varredura completa na lista ordenando todos os elementos.
# Vamos tomar a lista de tamanhao N, logo, dividindo ela em 3 partes nós temos n/3; n/3; n/3.
# Tomemos a = n/3; b = n/3; c = n/3.
# Como ordenamos primeiramente a + b, notamos que há  uma lista ordernada entre esses dois campos.
# Após isso, iremos ordenar b + c, com isso, temos que os maiores elementos estão no final. 
# Por fim, basta ordenar o restante a + b para ter a lista ordenada de forma completa.

# O tempo de execução será de o(n²).