# gerenciamento de elevador poo

class Elevador:
    '''
    Docstring para Elevador
    Classe que simula o funcionamento de um elevador em um predio residencial ou comercial.
    '''
    #Atributos
    def __init__(self, maximo_andares, maxima_capacidade):
        self.__andar_atual = 0
        self.__pessoas_presentes = 0
        self.__maximo_andares = maximo_andares
        self.__maxima_capacidade = maxima_capacidade
    
    #Metodos
        #Metodo subir - leva o elevador para o andar escolhido
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
            

        # Metodo descer - leva o elevador para o andar escolhido
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

               
           
        #Metodo entrar - adiciona pessoas ao elevador
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
           
           
        #Metodo sair - remove pessoas do elevador
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
    '''
    Docstring para getters
    Metodos que retornam os valores dos atributos privados da classe Elevador
    '''
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
    
#
#Clase filha 

class ElevadorDeCarga(Elevador):
    '''
    Docstring para ElevadorDeCarga
    Classe que simula o funcionamento de um elevador de carga em um predio comercial ou industrial.
    Extende a classe Elevador e adiciona funcionalidades especificas para o transporte de cargas.
    '''

    def __init__(self, maximo_andares, maxima_capacidade):
        super().__init__(maximo_andares,maxima_capacidade)
        self.__peso_atual = 0
    #Metodos Sobrescritos
    def entrar(self, carga):
        if self.__peso_atual + carga > self.maxima_capacidade:
            print("Peso excesivo !")

        else:
            self.__peso_atual += carga
            print(f"Carga liberada")        

    def sair(self, carga):
        if carga < 0:
            print("Erro! Carga invalida")

        elif carga > self.__peso_atual:
            print("Erro! Carga insuficiente para retirar")
        else:
            self.__peso_atual -= carga
            print("Carga retirada com sucesso")

    #Getter
    '''
    Docstring para getter
    Metodo que retorna o valor do atributo privado peso_atual da classe ElevadorDeCarga
    '''
    @property
    def peso_atual(self):
        return self.__peso_atual



# exemplo de composicao - predio com varios elevadores

class Predio:
    '''
    Docstring para Predio
    Classe que representa um predio com varios elevadores.
    Permite o gerenciamento e controle dos elevadores presentes no predio.
    '''
    def __init__(self, elevadores:list)-> None:

        self.__elevadores = elevadores


    #metdo painel de controle
    def painel_controle(self):
        for i,e in enumerate(self.__elevadores):
            match e:
                case ElevadorDeCarga():
                    print(f"{i+1} [CARGA]-> Esta no andar {e.andar_atual} , Carga atual: {e.peso_atual}kg")
                case Elevador():
                    print(f"{i+1} [SOCIAL]-> Esta no andar {e.andar_atual} , {e.pessoas_presentes}")


#criacao de elevadores e predio
lista_elevadores = [Elevador(25,11),ElevadorDeCarga(15,1000),Elevador(25,8),Elevador(25,5)]

#criacao do predio com os elevadores
edificio1 = Predio(lista_elevadores)

#painel de controle dos elevadores do predio

while True:
    #Menu principal
    menu = int(input("1. Ver Painel de Controle\n2. Operar elevador\n3.sair\n--> "))
    match menu:
        #Menu painel de controle
        case 1: 
            edificio1.painel_controle()
        case 2:
            #Menu operacao elevador
            for i, e in enumerate(lista_elevadores):
                print(f"{i + 1}° Elevador")
            menu_elevador = int(input("Selecione o elevador que deseja mexer: "))
            elevador_atual = lista_elevadores[menu_elevador - 1]
            match elevador_atual:
                #Menu operacao elevador de carga
                case ElevadorDeCarga():
                    operacao = int(input("1. Subir\n2. Descer\n3. Entrar Carga\n4. Sair Carga\n"))
                    match operacao:
                        case 1:
                            andar = int(input("Digite o andar que deseja subir: "))
                            elevador_atual.subir(andar)
                        case 2:
                            andar = int(input("Digite o andar que deseja descer: "))
                            elevador_atual.descer(andar)
                        case 3:
                            carga = float(input("Digite o peso da carga que vai entrar: "))
                            elevador_atual.entrar(carga)
                        case 4:
                            carga = float(input("Digite o peso da carga que vai sair: "))
                            elevador_atual.sair(carga)
                        case _:
                            print("Opcao invalida")
                #Menu operacao elevador social
                case Elevador():

                    operacao = int(input("1. Subir\n2. Descer\n3. Entrar\n4. Sair\n"))
                    match operacao:
                        case 1:
                            andar = int(input("Digite o andar que deseja subir: "))
                            elevador_atual.subir(andar)
                        case 2:
                            andar = int(input("Digite o andar que deseja descer: "))
                            elevador_atual.descer(andar)
                        case 3:
                            pessoas = int(input("Digite o numero de pessoas que vao entrar: "))
                            elevador_atual.entrar(pessoas)
                        case 4:
                            pessoas = int(input("Digite o numero de pessoas que vao sair: "))
                            elevador_atual.sair(pessoas)
                        case _:
                            print("Opcao invalida")
        case 3:
            print("Saindo do programa...")
            break
        case _: 
            print("Opcao invalida")
    

