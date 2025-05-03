# FURIA_BOT
- FuriaBot/FuriaBotEspecia
- Há dois tipos de programa do chat bot, um possuí caracteres especiais "FuriaBotEspecial", já o outro não apresenta os mesmos "FuriaBot"


## [SUMÁRIO](#sumário)

1. [Descrição](#descrição)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Guia](#guia)
4. [Como Usar](#como-usar)
5. [Requisitos](#requisitos)
6. [Diagrama Caso de Uso](#diagrama-caso-de-uso)

  
## 1. [Descrição](#descrição)
- O código tem o objetivo de simular uma conversa com um chat inteligente que disponibiliza ao usuário várias opções e respostas sobre os possíveis interesses de um torcedor de CS da Furia Esports.
- Destinado aos torcedores da Furia de Counter-Strike 2, o programa oferece varios tópicos que abrangem os interesses deles, como as redes sociais do time de CS, loja virtual de roupas e acessórios, e, principalmente, informações abrangentes dos times masculino e feminino da Furia:
1. Elenco - Nicks e nomes, idade e posição
2. Redes Sociais - Instagram, X/Twitter e Twitch
3. Configurações e Periféricos
4. Principais Troféis e Premiações - Nome campeonato, posição, premiação(US$)
5. Histórico/Últimos Jogos


     
## 2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
  1. Linguagem de Programação:
     - O programa foi desenvolvido utilizando Python, uma linguagem poderosa e versátil, ideal para automação e processamento de dados.
  2. Editor de Código: Visual Studio Code (VS Code)
     - A utilização de VS Code proporcionou um ambiente de desenvolvimento eficiente e prático, com funcionalidades como debugging e refatoração.
  3. Biblioteca:
     - Tabulate - A biblioteca tabulate foi utilizada para formatar e exibir dados tabulares de maneira legível e organizada no terminal.
     - Time - A biblioteca time foi utilizada para realizar medições de tempo, como em delays, temporizadores e cálculos de tempo de execução de trechos específicos do programa.



## 3. [Guia](#guia)
  Como Baixar o Programa:
  
1. Abra o repósitorio do GitHub: https://github.com/Rafael-Rase/FURIA_BOT/tree/main
2. Escolha qual versão do programa gostaria de usar, o FuriaBot ou o FuriaBotespecial
3. Clqieu sobre o nome do programa escolhido ".rar"
4. Clique no símbolo de download e baixe o arquivo winrar e extraia em uma pasta

  ### Como executar o programa:

- 'FuriaBot'.
1. Dê dois cliques no arquivo nome_do_arquivo.exe
2. Espere o terminal abrir e mostrar os dados
3. Se o terminal fechar rápido, abra o arquivo pelo Prompt de Comando para ver a saída completa

Atenção: O Windows pode mostrar um aviso de segurança. Clique em "Mais informações" > "Executar assim mesmo".

- 'FuriaBotEspecial'.
  - Ele precisa de um terminal diferente do padrão do windows, já que ele não consegue rodar com sua eficiência e importância no terminal clássico do Windows
Este programa funciona no console e usa:
- Emojis
- Acentos
- Cores e Negrito
- UTF-8

Siga os passos abaixo para executá-lo corretamente.


#### 0 - NAO TEM O WINDOWS TERMINAL INSTALADO?

1. Baixe gratuitamente na Microsoft Store:
   https://aka.ms/terminal
   
OU
2. Use o PowerShell que ja vem com o Windows:

   - Pressione Windows + R
   - Digite: powershell
   - Pressione Enter
   - Depois siga os mesmos passos abaixo

#### 1 - ABRA O WINDOWS TERMINAL

- Clique no menu Iniciar e digite:
  Windows Terminal

- Clique para abrir. Ele e melhor que o "cmd" antigo,
pois ja suporta UTF-8, emojis e formatacao moderna.

#### 2 - NAVEGUE ATE A PASTA DO PROGRAMA

Digite o endereço de campo que voce extraiu o programa no terminal :
- exemplo de endereço.

    cd C:\Python\FuriaBotEspecial\dist

Pressione Enter.

#### 3 - EXECUTE O PROGRAMA .EXE

No Windows Terminal ou PowerShell, voce deve usar:

    .\FuriaBotEspecial.exe

(tem que ter o ".\" no inicio - isso e obrigatorio no PowerShell)

Pressione Enter e o programa vai rodar.

#### 4 - O PROGRAMA MOSTROU INTERROGACOES (?) OU NAO COLORIU?

Isso pode acontecer se a fonte do terminal nao suportar emojis ou UTF-8 corretamente.

Para corrigir:

1. Clique na seta no canto superior da aba e selecione "Configuracoes"
2. Va em "Perfis" > "PowerShell" (ou CMD)
3. Em "Fonte", escolha uma das seguintes:

   - Cascadia Code PL (melhor)
   - Segoe UI Emoji
   - Consolas
   - Lucida Console

4. Salve e feche. Agora os emojis e cores devem aparecer corretamente.

#### 5 - ANTIVIRUS BLOQUEOU O PROGRAMA?

Por ser um arquivo .exe criado manualmente, alguns antivirus podem acusar falso positivo.

Se isso acontecer:

- Marque o programa como seguro
- Ou adicione uma excecao no antivirus



## 4. [Como Usar](#como-usar)
- O sistema possui uma fácil utilização, sua função se baseia em digitar a opção desejada e seguir o raciocínio e etapas do assistente virtual
- EXEMPLO:
  
![image](https://github.com/user-attachments/assets/a4e616ec-5583-46ab-a363-d58efebb1baf)

- O programa espera a digitação e confirmação do usuário:

![image](https://github.com/user-attachments/assets/c6d97785-1a77-4c51-ae13-3ef46cce2da5)

- O programa entende a responda e prossegue para próxima etapa

![image](https://github.com/user-attachments/assets/33c8312c-0ffc-453b-9038-e97c8a7a1921)

## 5. [Requisitos](#requisitos)
Foram solicitados diversos requisitos para integrar o uso de Inteligência Artificial nas tarefas, sendo esses os planejados após o levantamento de requisitos inicial da integração:

- Requisitos Funcionais:

RF01- A inteligência artificial deve categorizar os chamados dos clientes em diversas categorias para facilitar a direção do atendimento.

RF02- A inteligência artificial deve apresentar soluções simples e de fácil entendimento para resolver duvidas.

RF03- A inteligência artificial deve repassar o link de sites para confirmar e validar as fontes aos usuários.

RF05- A inteligência artificial deve passar o link de sites caso ele não consiga armazenar/informar completamente o assunto ao usuário.

- Requisitos Não Funcionais:

RNF01 - Facilidade de Uso: O sistema deve ser de fácil entendimento para aprendizado rápido do usuário.

RNF02 – Velocidade: Sistema necessita ser rápido e eficiente para uma melhor experiência do usuário.

RNF03 – Disponibilidade: O sistema deve ficar disponível a todo momento, e ficar apenas indisponível quando a conversa for encerrada.

RNF04 – Manutenibilidade: O código-fonte deve estar devidamente documentado para alterações ou correções necessárias.

## 6. [Diagrama Caso de Uso](#diagrama-caso-de-uso)

![image](https://github.com/user-attachments/assets/bc4a4d71-8ae7-4770-abe5-2f8fb2384bde)


