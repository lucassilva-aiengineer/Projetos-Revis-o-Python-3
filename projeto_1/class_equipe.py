from class_colaborador import Colaborador
from typing import Union, List

# Criando a classe equipe que é a agregagação de colaboradores 


class Equipe:

    def __init__(self, nome_equipe: str= "Nome da equipe", lider:  Union[Colaborador, str]= "Lider da equipe", 
                missao_equipe: str= "Missão da equipe", colaboradores: List[Colaborador]= [], custo_insumos: float= 0):

    # Este método é executado apenas na construção, instânciação, do objeto.

        # Aributos privados 
        self.__nome_equipe = nome_equipe 
        self.__lider = lider 
        self.__missao_equipe = missao_equipe 
        self.__colaboradores = colaboradores
        self.__custo_insumos = custo_insumos 
        self.__custo_operacional_total = 0


    # Criando as regras de encapsulamento. 
    # O encapsulamento é algo que nos permite interseptar o acesso do usuário as classes, tanto quando o usuário 
    # tenta definir algo ou tanto quando o usuário tenta ler algo, é como o guarda de fronteira que impede que 
    # o acesso seja irrestrito, verificando o acesso, sendo capaz de barrar a entrada ou saída de pessoas. 

    # Regras de acesso a leitura. 
    @property 
    def nome_equipe(self)-> str:
        return self.__nome_equipe 

    @property 
    def lider(self)-> Union[Colaborador, str]:
        return self.__lider

    @property 
    def missao_equipe(self)-> str:
        return self.__missao_equipe 

    @property 
    def colaboradores(self)-> List[Colaborador]:
        return self.__colaboradores 

    @property 
    def custo_insumos(self)-> float:
        return self.__custo_insumos

    @property 
    def custo_operacional_total(self):

        # Assim recalculamos o custo sempre que acessamos o atributo.
        return sum([colaborador.salario for colaborador in self.__colaboradores]) + self.__custo_insumos



    # Desenvolvendo os setters 
    # De quais formas os atributos poderão ser redefinidos, alterados?, temos algo intermediário, algo 
    # que está entre o atributo e a alteração que o usuátio propõe, o método setter. 

    @nome_equipe.setter 
    def nome_equipe(self, nv_nome: str)-> None:
        self.__nome_equipe = nv_nome

    @lider.setter 
    def lider(self, nv_lider: Union[Colaborador, str])-> None: 

        """ É bem interessante tratarmos o acesso a estes
            atributos de uma melhor forma. Por exemplo, exigindo uma senha 
        """
        self.__lider = nv_lider 

    @missao_equipe.setter 
    def missao(self, nv_missao)-> None:
        self.__missao_equipe = nv_missao

    @colaboradores.setter 
    def colaboradores(self, nvs_colaboradores)-> None:
        self.__colaboradores = nvs_colaboradores 

    @custo_operacional_total.setter
    def custo_operacional_total(self, nv_custo_operacional)-> None:

        """
            Da forma como tais métodos foram construidos, tem-se margem para a alteração 
            de qualquer atributo, por qualquer usuário, de forma muito simples. Evidentemente,
            isto deve ser mudado. 

        """
        self.__custo_operacional_total = nv_custo_operacional



    # Utilizando o método mágico __repr__ para criarmos algo que será retornado quando imprimirmos
    # a instância no lugar de simplesmente o endereço de memória. 

    def __repr__(self)-> str:
        return f"""{self.__nome_equipe} | n° de talentos {len(self.__colaboradores)}
Nossos talentos: {[str(colaborador.nome + " ,") for colaborador in self.__colaboradores]}"""



def teste_main():

    equipe_a = Equipe("Equipe Bravo",   Colaborador("Mateus", 
                                                    "24/02/1997", 
                                                    29, "000.000.000-00", "Líder de desenvolvimento",
                                                    "Lidera o desenvolvimento dos nossos produtos", 
                                                    "22/02/2010", salario= 40000), 
                    "Produção de novos produtos - P&D", custo_insumos= 30000)


    print(equipe_a)

    print(equipe_a.lider)
teste_main()

