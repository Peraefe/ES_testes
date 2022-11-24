class batimentosCardiacos:
    __nome='';
    __sobrenome='';
    __dianasc=0;
    __mesnasc=0;
    __anonasc=0;
    def _init_(self,nome=None,sobrenome=None,dia=None,mes=None,ano=None):
        if(type(nome)==type(str())):
            self.__nome=nome;
        if(type(sobrenome)==type(str())):
            self.__sobrenome=sobrenome;
        if(type(dia)==type(int())):
            self.__dianasc=dia;
        if(type(mes)==type(int())):
            self.__mesnasc=mes;
        if(type(ano)==type(int())):
            self.__anonasc=ano;
        return;

    def idade(self,dia=None,mes=None,ano=None):
        if(type(ano)==type(int()) and type(mes)==type(int()) and type(dia)==type(int())):
            if((mes==self.__mesnasc and dia>=self.__dianasc) or (mes>self.__mesnasc)):
                return ((ano)-(self.__anonasc));
            return ((ano-1)-(self.__anonasc));
    
    def frequencia_max(self,idade):
        if(type(idade)==type(int())):
            return (220-(idade));
    
    def mostradados(self):
        print("Nome: {}\nSobrenome: {}\nData de Nascimento: {}/{}/{}".format(self.__nome,self.__sobrenome,self.__dianasc,self.__mesnasc,self.__anonasc));
        
       
