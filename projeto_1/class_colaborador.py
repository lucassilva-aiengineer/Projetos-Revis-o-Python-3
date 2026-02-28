from class_pessoa import Pessoa 

class Colaborador(Pessoa):

    """
        Herdamos todos os métodos e atributos da classe 
        colaborador. 

    """


    def __init__(self, nome: str= "", data_nascimento: str= "", idade: int= 0, cpf: str= "", 
                cargo: str= "", data_admissao: str= "", ): 

        # Meio que criamos um objeto Base. 
        super().__init__(nome, data_nascimento, idade, cpf)

        # E especializamos como atributos e métodos próprios. 
        self.__cargo = 


    int numero = 0; 
# Escopo -> Design -> Build -> Testing -> Deploy 