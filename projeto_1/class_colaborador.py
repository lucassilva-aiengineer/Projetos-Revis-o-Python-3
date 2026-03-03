from class_pessoa import Pessoa 
from typing import List 


class Colaborador(Pessoa):

    """
        Herdamos todos os métodos e atributos da classe 
        colaborador. 

    """


    def __init__(self, nome: str= "", data_nascimento: str= "", idade: int= 0, cpf: str= "", 
                cargo: str= "", descricao_funcao: str= "",data_admissao: str= "", relatorios: List[str]= [],
                salario: float= 1518.00, historico_salarial: List[float]= []): 

        # Meio que criamos um objeto Base. 
        super().__init__(nome, data_nascimento, idade, cpf)

        # E especializamos como atributos e métodos próprios. 

        # Atributos Privados
        self.__cargo = cargo
        self.__data_adimissao = data_admissao 
        self.__descricao_funcao = descricao_funcao 
        self.__relatorios = relatorios
        self.__salario = salario
        self.__historico_salarial = historico_salarial 

    # Métodos de acesso de leitura
    @property 
    def cargo(self)-> str:
        return self.__cargo 

    @property
    def descricao_funcao(self)-> str:
        return self.__descricao_funcao 

    @property 
    def data_admissao(self)-> str:
        return self.__data_adimissao 

    @property 
    def relatorios(self)-> List[str]:
        return self.__relatorios 

    @property 
    def salario(self)-> float:
        return self.__salario

    @property 
    def historico_salarial(self)-> List[float]:
        return self.__historico_salarial 



    # Métodos de acesso de escrita, aqui temos uma fronteira entre a escrita dos 
    # atributos, reescrita dos atributos. 

    @cargo.setter 
    def cargo(self, nv_cargo)-> None:
        self.__cargo = nv_cargo 


    @data_admissao.setter 
    def data_admissao(self, nv_data_admissao)-> None:

        # Se não tem return return None. 

        self.__data_adimissao = nv_data_admissao 

    @descricao_funcao.setter 
    def descricao(self, nv_descricao)-> None:
        self.__descricao = nv_descricao 


    @relatorios.setter 
    def relatorios(self, nv_relatorios)-> None: 
        self.__relatorios = nv_relatorios 


    @salario.setter 
    def salario(self, nv_salario)-> None:
        self.__salario = nv_salario 

    @historico_salarial.setter 
    def historico_salarial(self, nv_historico_salarial)-> None:
        self.__historico_salarial = nv_historico_salarial 


    # def __repr__(self)-> str:
    #     return f"Nome {self.__nome}"     # Este método já está sendo herdado da classe mãe. 

    def relatorio_colaborador(self)-> str:
        """
            Este Método fornece um relatório com 
            informações valiosas sobre o objeto colaborador 
            sobre o colaborador. 

        """


        return f"""
=========================== Relatório ==========================
Nome: {self.nome}               Data Admissão: {self.__data_adimissao}
Idade: {self.idade}             Data de Nascimeto: {self.data_nascimento}
================================================================
Descrição da função: {self.__descricao_funcao}


Relatório Mais Recente: {self.__relatorios[-1] if len(self.__relatorios) else "Sem relatóro"}"""




# Escopo -> Design -> Build -> Testing -> Deploy 


# Testando objeto colaborador 

def testes():

    descricao = """
                    Análisa e extrai conhecimento dos dados da GeneriCompany, os dados princípalmente 
                    relacionados as vendas da empresa, com foco na predição e na prescrição. 
                """

    colaborador_teste = Colaborador("Marcos", "02/03/2004", 21, "000.000.000.00",
                                    "Ciêntista de Dados", descricao, "02/01/2026",
                                    salario= 20000.40)


    print(colaborador_teste)

    print(colaborador_teste.relatorio_colaborador())

