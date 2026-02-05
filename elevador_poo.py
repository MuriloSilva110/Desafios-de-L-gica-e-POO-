from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
import time
from rich.layout import Layout
from rich.align import Align

console = Console()


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
                console.print(f"[red]Erro! nao e possivel descer , elevador parado[/red]")

            elif andar_escolhido == self.__andar_atual:
                console.print(f"[yellow]O elevador ja esta no {self.__andar_atual}° Andar[/yellow]")
            
            else:
                distancia = andar_escolhido - self.__andar_atual
                console.print(f"\n[bold cyan]Iniciando subida para o {andar_escolhido}° andar...[/bold cyan]")
                for passo in track(range(distancia), description="[green]Subindo...[/green]"):
                    time.sleep(0.5)  # Simula o tempo de subida


                self.__andar_atual = andar_escolhido
                console.print(f"[bold green]✅ Elevador parado no {self.andar_atual}° Andar![/bold green]\n")

        else:
            console.print(f"[bold red]🚫 Erro:[/bold red] O andar {andar_escolhido}° não existe neste prédio.")
            

        # Metodo descer - leva o elevador para o andar escolhido
    def descer(self, andar_escolhido):

        if andar_escolhido >=0 and andar_escolhido <=self.__maximo_andares:
            
            if andar_escolhido > self.__andar_atual:
                console.print(f"[red]Erro! nao e possivel subir , elevador parado[/red]")
            
            elif andar_escolhido == self.__andar_atual:
                console.print(f"[yellow]O elevador ja esta no {self.__andar_atual}° Andar[/yellow]")
            else:
                distancia = self.__andar_atual - andar_escolhido
                console.print(f"\n[bold cyan]Iniciando descida para o {andar_escolhido}° andar...[/bold cyan]")
                for passo in track(range(distancia), description="[green]Descendo...[/green]"):
                    time.sleep(0.5)  # Simula o tempo de descida

                self.__andar_atual = andar_escolhido
                console.print(f"[bold green]✅ Elevador parado no {self.andar_atual}° Andar![/bold green]\n")

        else:
            console.print(f"[bold red]🚫 Erro:[/bold red] O andar {andar_escolhido}° não existe neste prédio.")        

               
           
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
        table = Table(title="🏢 PAINEL DE CONTROLE - STATUS DOS ELEVADORES ", show_header=True, header_style="bold cyan")
        table.add_column("N° Elevador",justify="center",style="white")
        table.add_column("Tipo",justify="center",style="magenta")
        table.add_column("Andar Atual",justify="center",style="green")
        table.add_column("Ocupaçao/Carga",justify="center",style="yellow")
        for i,e in enumerate(self.__elevadores):
            match e:
                case ElevadorDeCarga():
                    table.add_row(f"{i+1}", "Carga", f"{e.andar_atual}", f"{e.peso_atual}kg")
                case Elevador():
                    table.add_row(f"{i+1}", "Social", f"{e.andar_atual}", f"{e.pessoas_presentes} pessoas")
        console.print(table)


def splash_screen():
    console.clear()
    
    mensagem_abertura = Panel(
        Align.center(
            "\n[bold blue]🏢 SISTEMA DE GESTÃO PREDIAL[/bold blue]\n"
            "[white]Versão 2.0 - Desenvolvido por Murilo Silva[/white]\n"
            "[cyan]Status: Aguardando Inicialização...[/cyan]\n",
            vertical="middle"
        ),
        border_style="bright_blue",
        padding=(1, 2)
    )
    
    # 1. Imprime o painel apenas uma vez
    console.print(mensagem_abertura)
    
    # 2. Pergunta ao usuário
    confirmacao = Prompt.ask(
        "[bold yellow]Deseja iniciar o sistema agora?[/bold yellow]", 
        choices=["s", "n"], 
        default="s"
    )
    
    if confirmacao.lower() == 's':
        # 3. Em vez de limpar e imprimir de novo, apenas mostramos o status abaixo
        with console.status("[bold green]Sincronizando elevadores e sensores...[/bold green]", spinner="bouncingBar"):
            time.sleep(2)
        
        # 4. Limpa apenas quando for entrar no Menu Principal do loop while
        console.clear()
    else:
        console.print("[bold red]Inicialização cancelada pelo usuário.[/bold red]")
        exit()

splash_screen()

#criacao de elevadores e predio
lista_elevadores = [Elevador(25,11),ElevadorDeCarga(15,1000),Elevador(25,8),Elevador(25,5)]

#criacao do predio com os elevadores
edificio1 = Predio(lista_elevadores)

#painel de controle dos elevadores do predio

while True:
    console.clear() # Limpa a tela ao iniciar ou voltar ao menu principal
    
    console.print(Panel.fit(
        "1. Ver Painel de Controle\n2. Operar Elevador\n3. Sair",
        title="[bold blue]🏢 SISTEMA PREDIAL[/bold blue]",
        border_style="cyan"
    ))
    
    menu = IntPrompt.ask("Escolha uma opção", choices=["1", "2", "3"])

    match menu:
        case 1: 
            console.clear()
            edificio1.painel_controle()
            Prompt.ask("\nPressione [bold]Enter[/bold] para voltar ao menu") # Pausa para leitura
            
        case 2:
            console.clear()
            console.print("\n[bold magenta]Lista de Elevadores Disponíveis:[/bold magenta]")
            for i, e in enumerate(lista_elevadores):
                tipo = "📦 CARGA" if isinstance(e, ElevadorDeCarga) else "👥 SOCIAL"
                console.print(f"[white]{i + 1}° Elevador - {tipo}[/white]")
            
            menu_elevador = IntPrompt.ask("\nSelecione o número do elevador")
            elevador_atual = lista_elevadores[menu_elevador - 1]
            
            console.clear() # Limpa para mostrar o menu específico do elevador escolhido
            
            match elevador_atual:
                case ElevadorDeCarga():
                    console.print(Panel("[bold yellow]Menu: ELEVADOR DE CARGA[/bold yellow]"))
                    operacao = IntPrompt.ask("1. Subir\n2. Descer\n3. Entrar Carga\n4. Sair Carga", choices=["1", "2", "3", "4"])
                    
                    match operacao:
                        case 1:
                            andar = IntPrompt.ask("Digite o andar que deseja subir")
                            elevador_atual.subir(andar)
                        case 2:
                            andar = IntPrompt.ask("Digite o andar que deseja descer")
                            elevador_atual.descer(andar)
                        case 3:
                            carga = float(Prompt.ask("Digite o peso da carga (kg)"))
                            elevador_atual.entrar(carga)
                        case 4:
                            carga = float(Prompt.ask("Digite o peso da carga para retirar (kg)"))
                            elevador_atual.sair(carga)
                    
                    Prompt.ask("\nOperação finalizada. Pressione [bold]Enter[/bold] para continuar")

                case Elevador():
                    console.print(Panel("[bold green]Menu: ELEVADOR SOCIAL[/bold green]"))
                    operacao = IntPrompt.ask("1. Subir\n2. Descer\n3. Entrar\n4. Sair", choices=["1", "2", "3", "4"])
                    
                    match operacao:
                        case 1:
                            andar = IntPrompt.ask("Digite o andar que deseja subir")
                            elevador_atual.subir(andar)
                        case 2:
                            andar = IntPrompt.ask("Digite o andar que deseja descer")
                            elevador_atual.descer(andar)
                        case 3:
                            pessoas = IntPrompt.ask("Quantas pessoas vão entrar?")
                            elevador_atual.entrar(pessoas)
                        case 4:
                            pessoas = IntPrompt.ask("Quantas pessoas vão sair?")
                            elevador_atual.sair(pessoas)
                    
                    Prompt.ask("\nOperação finalizada. Pressione [bold]Enter[/bold] para continuar")

        case 3:
            console.print("[bold red]Encerrando o sistema predial... Até logo![/bold red]")
            time.sleep(1)
            break
        
        case _:
            console.print("[bold red]Opção inválida! Por favor, escolha uma opção válida.[/bold red]")

