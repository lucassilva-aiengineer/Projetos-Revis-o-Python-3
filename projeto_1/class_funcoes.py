import string 
from typing import List 
import random 
import time 

class Funcoes:

    @staticmethod
    def gerar_id()-> str:

        letras: List[str] = []

        letras += string.ascii_lowercase + string.ascii_uppercase 

        id_ = ""

        caracteres_gerados, caracter_gerar = 0, 10
        while caracteres_gerados < caracter_gerar:

            if random.randint(0, 1) == 0:
                random.shuffle(letras)

            else: 
                pass 




        return id_


def main():

    # Testes 

    def testes_modulo_string()-> None:
        lista_carcteres = []
        lista_carcteres += string.ascii_lowercase 

        print(lista_carcteres)

        print(string.ascii_uppercase)

        # print(["Pessoa"])

        lista_pessoa: List[str] = []
        nome = "Lucas"

        lista_pessoa += nome

        print(lista_pessoa)


    def teste_randint()-> None:

        iteracoes_executadas = 0

        numero = 0
        while numero != 1:
            numero = random.randint(0, 1)
            print(numero)

            if iteracoes_executadas == 10:
                print("Saindo...")
                time.sleep(2)

                print("Execuções efetuadas: ", 10, sep= "")
                break 
            print("Iterações Executadas: ", iteracoes_executadas)

            iteracoes_executadas += 1

    # teste_randint() 

    def teste_randint_pro()-> None:

        tentativas = 0
        while True:

            if tentativas < 10: 

                numero = random.randint(0, 1)

                if numero != 1:
                    print("Um número diferente do 1 foi encontrado!")
                    time.sleep(1)

                    print("Tentando novamente...")
                    time.sleep(1)

                    tentativas += 1

                else:
                    print("Número encontrado!")
                    time.sleep(1)

                    print("Número: " + str(numero))
                    time.sleep(2)

                    print("Tentativas realizadas: ", tentativas)
                    break 

            else: 
                print("Número de tentativas excedidas!")
                time.sleep(2)

                print("Encerrando iteração...")
                time.sleep(1)

                print("Número tentativas: ", tentativas)
                time.sleep(2)
                break 

    # teste_randint_pro() 

    # Forma mais pythonic 

    def teste_randint_pro_max()-> None: 

        while True:

            numero = random.randint(0, 1)
            break 

if __name__ == '__main__':
    main()