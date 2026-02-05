# Desafios de Lógica e POO - Python 🐍

Este repositório é o meu "laboratório" de desenvolvimento pessoal. Aqui reúno diversos desafios de programação e exercícios práticos realizados durante a graduação em **Análise e Desenvolvimento de Sistemas (Unisa)**. O objetivo é consolidar os fundamentos de Python, focando em autonomia, escrita de código limpo e resolução de problemas reais sem o uso de geradores automáticos de código.

## 🚀 Objetivo
Treinar a aplicação de padrões de projeto, o domínio da documentação oficial do Python e a criação de interfaces de linha de comando (CLI) profissionais e intuitivas.

---

## 📂 Desafios Disponíveis

### 1. Sistema de Gestão de Elevadores (`elevador_poo.py`)
Um simulador robusto que evoluiu de uma lógica simples para um sistema de gestão predial complexo com interface visual polida.

* **Herança e Polimorfismo**: Implementação da classe `ElevadorDeCarga` que herda de `Elevador`, adaptando métodos para gestão de peso (kg) em vez de passageiros.
* **Composição**: Classe `Predio` que gerencia uma frota de diferentes elevadores de forma centralizada.
* **Encapsulamento**: Uso rigoroso de atributos privados e Decorators (`@property`) para proteção de dados.
* **Interface Moderna (Rich Library)**:
    * **Splash Screen**: Tela de abertura interativa com carregamento simulado e prompt de confirmação.
    * **Painel de Controle**: Monitoramento em tempo real do status dos elevadores através de tabelas estilizadas.
    * **Feedback Visual**: Uso de barras de progresso (`track`) para simular o deslocamento físico entre os andares e limpeza automática do console para melhor navegabilidade.
* **Controle de Fluxo**: Uso de `match/case` (Python 3.10+) para menus limpos e redução de complexidade de condicionais.

### 2. (Próximo Desafio...)
*(Espaço reservado para os próximos exercícios de lógica!)*

---

## 🛠️ Tecnologias e Ferramentas
* **Linguagem**: Python 3.10+ (utilizando Modern Patterns).
* **Bibliotecas**: [Rich](https://github.com/Textualize/rich) (para interface CLI avançada).
* **Conceitos**: POO Avançada, Gestão de Estados, UX no Terminal e Docstrings profissionais.
* **Ambiente**: VS Code e Git.

## ⚙️ Como Executar
Este projeto utiliza a biblioteca **Rich**. Para rodar o simulador corretamente, siga os passos abaixo:

1. Instale a dependência:
   ```bash
   pip install rich

2. Execute o arquivo:
   ```bash 
   python elevador_poo.py


🔗 Outros Projetos Principais
Confira também meus projetos de maior escala e aplicações completas:

[Gerenciador de Estoque Full Stack](https://github.com/MuriloSilva110/projeto_estoque_web) – Aplicação Web com Flask, SQL e Deploy.

[Automação de Testes com Selenium](https://github.com/MuriloSilva110/stock-manager-selenium-automation) – Scripts de teste E2E com mimetismo humano.

👤 Autor
Murilo Silva Estudante de ADS na Unisa | Conclusão em 12/2026

[LinkedIn:](linkedin.com/in/murilo-silva-dev/)
