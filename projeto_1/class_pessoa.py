

class Pessoa:

    def __init__(self, nome: str= "", data_nascimento: str= "", idade: int= 0 , cpf: str= ""):

    # Atributos privados 
        self.__nome = nome 
        self.__data_nascimento = data_nascimento 
        self.__idade = idade 
        self.__cpf = cpf 



    # Encapsulamento 
    # Algo bem como um oficial de fronteira que impede o acesso irrestrito 
    # tanto para com a escrita quanto para com a leitura. 

    # Getters - Métodos de acesso a leitura. 
    @property 
    def nome(self)-> str:

        """
            Aqui nós utilizamos essa intermediação entre o atributo do objeto 
            e o usuário e, no caso específico, nós impedirmos que as primeiras casas sejam vistas 
            livremente.
        """

        # parte_a = ['*' for a in self.__nome[:3]]
        # parte_a.extend([self.__nome[2:]])

        parte_a = [self.__nome[:3]]
        parte_a.extend(["*" for letra in self.__nome[3:]])

        nome_formatado = "".join(parte_a)

        return nome_formatado


    @property 
    def data_nascimento(self)-> str:
        return self.__data_nascimento


    @property 
    def idade(self)->str:
        return self.__idade 


    @property 
    def cpf(self)-> str:
        return self.__cpf 


    # Setters - Escrição dos atributos 

    @nome.setter 
    def nome(self, nv_nome)-> None:

        # Vetamos o acesso a escrita, temos como intermediar o acesso 
        # a escrita. 

        nomes = ["Marcos", "Jonas", "João"]

        if len(nv_nome) > 3:
            if not nv_nome in nomes:
                self.__nome = nv_nome

            else: 
                print("Nome não Autorizado!")

        else:
            print("Os nomes indicados devem possuir mais de três caracteres.")

    @data_nascimento.setter 
    def data_nascimento(self, nv_data_nascimento)-> None:
        self.__data_nascimento = nv_data_nascimento 


    @idade.setter 
    def idade(self, nv_idade)-> None:
        self.__idade = nv_idade


    @cpf.setter 
    def cpf(self, nv_cpf)-> None:
        self.__cpf = nv_cpf


    # Utilizando o método mágico ou dunder, double underscore. 

    def __repr__(self)->str:
        return f"Nome: {self.__nome} | Idade: {self.__idade}"


def main():

    """
        Testando a criação dos objetos. 
    """


    objeto = Pessoa("Jonathas", "20/10/25", 20, "000.000.000.00")

    # print(objeto)

    # print(objeto) 

    # Acessando o atributo do objeto. 
    print(objeto.nome)


    # Tentando alterar o atributo nome 

    objeto.nome = "Jonas"
    print(objeto.nome)

    objeto.nome = "Luc"
    print(objeto.nome)

    objeto.nome = 'Davi'

    print(objeto.nome)

# main()