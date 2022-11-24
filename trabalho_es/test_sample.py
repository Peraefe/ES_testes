from moduloq03 import *

#testando as funções
p1=batimentosCardiacos();
p1._init_('Ana','Silva',1,5,2000);

def test_idade():
    assert p1.idade(22,11,2022) == 22

def test_frequencia():
    assert p1.frequencia_max(p1.idade(22,11,2022)) == 198

def test_mostraDados():
    assert p1.mostradados()==print("Nome: Ana\nSobrenome: Silva\nData de Nascimento: 1/5/2000")