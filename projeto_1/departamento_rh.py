from typing import List, Union, Optional
from class_colaborador import Colaborador 


class DepartamentoRh:

    def __init__(self, lider_rh: Union[Colaborador, str]= "Colaborador", times: List[Optional[List[Colaborador]]] = None,
        colaboradores: List[Colaborador]= []):


        # Criamos atributos, indicamos atributos ao endereço de memória do objeto, "self", 
        # e indicamos.  
        self.__id_ = None
        self.__lider = lider_rh 
        self.__times = times 
        self.__colaboradores = colaboradores 


    # Desenvolvendo as regras de acesso que definem a nosso encapsulamento. 

    @property 
    def nome(self)-> str:
        return self.__id_ # Logo mais, alteratei o None para str. 

    @property 
    def lider(self)-> Union[str, Colaborador]:
        return self.__lider 

    @property 
    def times(self)-> List[Optional[List[Colaborador]]]: # Retornamos um tipo de dados optional, ora uma lista de colaboradores ora uma lista de None
        return self.__times 

    @property 
    def colaboradores(self)-> List[Colaborador]:
        return self.__colaboradores 



    def relatorio(self):

        """Esse método exibirá um relatório com as princípais 
            informações relacionadas aos times e aos funcionários, 
            sendo estas: valor da folha de pagamento, amplitude
            dos salários, a diferença entre o maior e o menor salário.
        """

        total_folha_pagamento = [for salario in self.__colaboradores] # Percorremos o atributo 
        # da classe colaboradores e pegamos de cada um desses objetos o atributo, ou será melhor 
        # apenas somarmos os custos operacionais? 



        return f"""
            
        """
        pass 