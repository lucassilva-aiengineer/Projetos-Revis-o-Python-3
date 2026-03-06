from class_colaborador import Colaborador 
import random 


# Um arquivo destinado a testes  


colaboradores = [Colaborador(salario= random.uniform(1800, 20000)) for _ in range(10)]



colaboradores_ordenados = sorted(colaboradores, key= lambda colaborador: colaborador.salario, reverse= True)

# print(colaboradores[:3])

for colaborador in colaboradores_ordenados:
    print(colaborador.salario)