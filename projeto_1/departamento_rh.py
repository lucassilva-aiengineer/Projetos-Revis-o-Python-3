from typing import List, Union, Optional
from class_colaborador import Colaborador 


class DepartamentoRh:

    def __init__(self, lider_rh: Union[Colaborador, str]= "Colaborador", times: List[List[Colaborador]] = [],
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
    def times(self)-> List[[List[Colaborador]]]: # Retornamos um tipo de dados optional, ora uma lista de colaboradores ora uma lista de None
        return self.__times 

    @property 
    def colaboradores(self)-> List[Colaborador]:
        return self.__colaboradores 



    def relatorio(self)-> str:

        """Esse método exibirá um relatório com as princípais 
            informações relacionadas aos times e aos funcionários, 
            sendo estas: valor total da folha de pagamento, amplitude
            dos salários, a diferença entre o maior e o menor salário.
        """

        folha_pagamento = [colaborador.salario for colaborador in self.__colaboradores]# Percorremos o atributo 
        # da classe colaboradores e pegamos de cada um desses objetos o atributo, ou será melhor 
        # apenas somarmos os custos operacionais? 

        total_folha_pagamento = sum(folha_pagamento)

        maior_salario = max(folha_pagamento)
        menor_salario = min(folha_pagamento) 

        # Quem ganha os três maiores salários 

        # Ordenando os colaboradores pelo valor do salário. 
        colaboradores_maiores_salarios = sorted(self.colaboradores, key= lambda colaborador: colaborador.salario, reverse= True)

        amplitude = maior_salario - menor_salario # A diferença entre o maior e o menor salário

        return f"""====================================================================
ID Departamento de RH: {self.__id_}
Lider Departamento: {self.__lider}
Quantidade de times: {sum([1 for a in self.__times])}
====================================================================

Total Folha de pagamento: {total_folha_pagamento}
Maior Salário: {maior_salario}
Menor Salário: {menor_salario}
"""
def main():
    pass 



if __name__ == '__main__':
    main()