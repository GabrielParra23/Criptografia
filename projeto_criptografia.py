from logo import logo



print(logo)

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


fim = "sim"
while fim == "sim":
    
    direcao = input("Quer encriptar ou descriptar:\n").lower()
    text = input("Escreva sua mensagem:\n").lower()
    shift = int(input("Escolha um numero:\n"))




    def cesar(texto, numero, escolha):
        """Aqui pode ser feito uma docstring para explicar oque essa função faz"""
        
        codigo = ""
        if numero > 26:
            numero = numero % 26
        for letra in texto: 
            if escolha == "encriptar":
                if letra == " " or letra not in alfabeto:
                    codigo += letra
                else:
                    local = alfabeto.index(letra)
                    codigo += alfabeto[local+numero]    
            elif escolha == "descriptar":
                if letra == " " or letra not in alfabeto:
                    codigo += letra
                else:
                    local = alfabeto.index(letra)
                    codigo += alfabeto[local-numero]
            else: 
                print("Escolha uma das opções")
                break
        
        print(f"sua mensagem {direcao} é {codigo}")
    
    cesar(texto = text, numero= shift, escolha = direcao)
    fim = input("se deseja continuar digite \"Sim\" se deseja terminar digite \"Não\"").lower()