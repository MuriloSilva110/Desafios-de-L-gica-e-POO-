# gerenciamento de elevador poo

class Elevador:
    #Atributos
    def __init__(self, maximo_andares, maxima_capacidade):
        self.__andar_atual = 0
        self.__pessoas_presentes = 0
        self.__maximo_andares = maximo_andares
        self.__maxima_capacidade = maxima_capacidade
    
    #Metodos
    def subir(self,andar_escolhido:int=0):
    
        if 0 <= andar_escolhido <= self.__maximo_andares:

            if andar_escolhido < self.__andar_atual :
               print(f"Erro! nao e possivel descer , elevador parado")

            elif andar_escolhido == self.__andar_atual:
                print(f"O elevador ja esta no {self.__andar_atual}° Andar")
            
            else:

                self.__andar_atual = andar_escolhido
                print(f"Elevador Subindo.....")
                print(f"Elevador parado...{self.__andar_atual}° Andar")

        else:
            print(f"Este andar {andar_escolhido}° nao esxite neste predio ")
            


    def descer(self, andar_escolhido):
        if andar_escolhido >=0 and andar_escolhido <=self.__maximo_andares:
            
            if andar_escolhido > self.__andar_atual:
                print(f"Erro! nao e possivel subir , elevador parado")
            
            elif andar_escolhido == self.__andar_atual:
                print(f"O elevador ja esta no {self.__andar_atual}° Andar")
            else:
                self.__andar_atual = andar_escolhido
                print(f"Elevador descendo.....")
                print(f"Elevador parado...{self.__andar_atual}° Andar")

        else:
            print(f"Este andar {andar_escolhido}° nao esxite neste predio ")        

               
           

    def entrar(self, pessoas):
        if pessoas > 0 and pessoas <=self.__maxima_capacidade:
            if self.__pessoas_presentes + pessoas > self.__maxima_capacidade:
               vagas_livres = self.__maxima_capacidade - self.__pessoas_presentes
               print(f"somente {vagas_livres} pessoas podem entrar.")
               print(f"Limite de peso ja execedido, {pessoas - vagas_livres} pessoas fcaram de fora")
            
            else:
                self.__pessoas_presentes += pessoas
                print(f"{pessoas} pessoas entram. ")

        else:
           print("Erro!, digite apenas numeros inteiros ")
           
           

    def sair(self,pessoas):
        if pessoas > 0 and pessoas <=self.__maxima_capacidade:
            if pessoas > self.__pessoas_presentes:
                print(f"Erro! NAO PODE SAIR MAIS PESSOAS QUE ESTAO PRESENTES ")

            else: 
                self.__pessoas_presentes -= pessoas
                print(f"{pessoas} pessoas Sairam.")
        else:
            print("Dgite apenas numeros inteiros")

    #Getters
    @property
    def maximo_andares(self):
        return self.__maximo_andares
    
    @property
    def maxima_capacidade(self):
        return self.__maxima_capacidade
    
    @property
    def andar_atual(self):
        return self.__andar_atual
    
    @property
    def pessoas_presentes(self):
        return self.__pessoas_presentes
    
#Testando o codigo
    

ev1 = Elevador(15,10)
print(f"Maximo de andares: {ev1.maximo_andares}°")
print(f"Maxima capacidade: {ev1.maxima_capacidade} pessoas")
ev1.entrar(8)
ev1.subir(5)
print(f"Andar atual: {ev1.andar_atual}°")
print(f"Pessoas presentes: {ev1.pessoas_presentes}")
ev1.entrar(6)
ev1.subir(13)
print(f"Andar atual: {ev1.andar_atual}°")
print(f"Pessoas presentes: {ev1.pessoas_presentes}")
ev1.entrar(5)
ev1.descer(8)
print(f"Andar atual: {ev1.andar_atual}°")
print(f"Pessoas presentes: {ev1.pessoas_presentes}")
ev1.sair(6)
ev1.descer(0)
ev1.sair(5)

