from moduloq03 import *

nome=input("Digite o nome: ");
sobrenome=input("Digite o sobrenome: ");
dia=int(input("Digite o dia do nascimento: "));
mes=int(input("Digite o mes do nascimento: "));
ano=int(input("Digite o ano do nascimento: "));

p1=batimentosCardiacos();
p1._init_(nome,sobrenome,dia,mes,ano);
p1.mostradados();
print("Idade: ",p1.idade(22,11,2022)); #idade recebe a data atual 22/11/2022
print("Frequência cardíaca máxima: ",p1.frequencia_max(p1.idade(22,11,2022)));



