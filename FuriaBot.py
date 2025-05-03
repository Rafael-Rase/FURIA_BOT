from tabulate import tabulate
import time

print("\n"*2)
print("          ##++        @@####                 \n" \
       "          ##############@@  ########..      \n" \
       "            mm########################MM    \n" \
       "        ################################    \n" \
       "      ################################mm    \n" \
       "    ##########################    ####      \n" \
       "    ########################                \n" \
       "  ##########################                \n" \
       "  ############@@##############MM  @@        \n" \
       "    ##################################      \n" \
       "  mm##############  ----      --####        \n" \
       "  mm##################                      \n" \
       "    ################                        \n" \
       "    ################                        \n" \
       "      @@############                        \n" \
       "        ##############                      \n" \
       "          ##############                    \n" \
       "              ##  @@####..                  \n")          
# Imprime uma arte ASCII simples com o tema FURIA.


print("\n")
print("OLA, BEM-VINDO AO CHAT FEITO PARA FAS FURIOSOS!")
print("Este chat e feito para mostrar informacoes relevantes sobres as \nprincipais lineups da FURIA")
time.sleep(1)

# Tabela inicial de escolhas de modalidades de e-sports da FURIA.
tabela_lineup = [
    ["1- Counter-Strike","Jogo de tiro tatico","Disponivel"],
    ["2- Valorant","Jogo de tiro tatico", "Indisponivel"],
    ["3- League of Legends","Moba", "Indisponivel"],
    ["0- SAIR"]
] 

cabecalho_tabela_lineup = ["LINEUPS","GENERO","ACESSO"]
cabecalho_tabela_opcoes = ["OPCAO"]
escolha = 1

print("\nPARA COMECAR,", end=" ")

# Primeiro laço de repetição (loop principal do programa).
while True:
    print("ESCOLHA UMA OPCAO") 
    time.sleep(1)

   
    print (tabulate(tabela_lineup[0:3], headers=cabecalho_tabela_lineup, tablefmt='grid'), )
    print (tabulate(tabela_lineup[3:], headers=cabecalho_tabela_opcoes, tablefmt='grid'))

    #Esperando resposta
    escolha = input("LINEUP [1, 2, 3, 0]: ") 
    
    # Uso do bloco "try" para lidar com possíveis erros se o usuário inserir um valor não inteiro.
    try:
        if int(escolha) == 1:
            print(" \nVoce escolheu a lineup de COUNTER-STRIKE", end= " ")
            time.sleep(1)
            print("ESTA DISPONIVEL!\nVamos prosseguir...\n")          
            time.sleep(1)

            # Tabela secundária de escolhas, apresentada após o usuário escolher Counter-Strike.
            tabela_cs_lineup = [
                ["1- Furia Masculino"], 
                ["2- Furia Feminino"],
                ["3- Redes Sociais"],
                ["4- Loja Virtual"],
                ["0- VOLTAR"]
            ]
            
            cabecalho_tabela_cs_lineup = ["LINEUP"]
            cabecalho_tabela_cs_opcoes = ["OPCOES"]           

            print("="*60)

            # Segundo laço de repetição (loop para as opções de Counter-Strike).
            while True:

                # Terceira tabela de escolhas, apresentada após escolher Counter-Strike.
                tabela_cs_lineups_opcoes = [
                                ["1- Elenco"],
                                ["2- Redes Sociais (LINK)"],
                                ["3- Configuracoes e Perifericos (LINK)"],
                                ["4- Trofeis e Premiacoes"],
                                ["5- Ultimos Jogos (LINK)"],
                                ["0- VOLTAR"]
                            ]
           
                cabecalho_tabela_cs_times = ["NICK", "NOME", "IDADE","POSICAO"]
                cabecalho_tabela_cs_rede = ["X/TWITTER","INSTAGRAM","TWITCH"]
                cabecalho_time_cs = ["CAMPEONATO", "ANO", "COLOCACAO", "PREMIACAO (US$)"]

                print("DO QUE VOCE GOSTARIA DE SE INFORMAR?")
                time.sleep(1)

             
                print (tabulate(tabela_cs_lineup[0:2], headers=cabecalho_tabela_cs_lineup, tablefmt='grid'))
                print (tabulate(tabela_cs_lineup[2:5], headers=cabecalho_tabela_cs_opcoes, tablefmt='grid'))
                escolha= input("OPCOES [1, 2, 3, 4, 0]: ") 
                try:
                    if int(escolha) == 1:
                        time.sleep(1)

                        
                        print("\nCarregando informacoes do TIME MASCULINO DE COUNTER-STRIKE")
                        time.sleep(1)
                        print("Informacoes tiradas dos sites (Atualizado/Verificado ultima vez em maio):")
                        print("\n-> https://www.hltv.org/team/8297/furia")
                        print("-> https://prosettings.net/teams/furia/#game-468")
                        print("-> https://bo3.gg/teams/furia \n")

                        time.sleep(1.5)
                        print("="*60)

                        # Terceiro laço de repetição (loop para as opções do time masculino).
                        while True:
                           
                 
                            tabela_cs_masculino = [
                                ["br FalleN (C)","Gabriel Toledo","33","Jogador"],
                                ["br yuurih ","Yuri Santos ","25","Jogador "],
                                ["lv YEKINDAR ","Mareks Gaļinskis ","25","Jogador "],
                                ["br KSCERATO ","Kaike Cerato ","25","Jogador "],
                                ["kz molodoy ","Danil Golubenko ","20","Jogador "],
                                ["br sidde "," Sid Macedo ","28","Coach "]
                            ]
                            
                            tabela_rede_social_masculino = [
                                ["x.com/i/user/112897001","https://www.instagram.com/fallen","https://www.twitch.tv/gafallen"],
                                ["https://x.com/yuurih ","https://www.instagram.com/yuurihfps "],
                                ["https://x.com/yek1ndar ","https://www.instagram.com/yek1ndar ","https://www.twitch.tv/yekindar "],
                                ["https://x.com/kscerato ","https://www.instagram.com/kscerato "],
                                ["https://x.com/tvoy_molodoy "],
                                ["https://x.com/siddecs ","https://www.instagram.com/siddecs/ "],
                                
                             ]
                            
                            print("DO QUE VOCE GOSTARIA DE SE INFORMAR?")
                            time.sleep(1)
                            print (tabulate(tabela_cs_lineups_opcoes, headers=cabecalho_tabela_cs_opcoes, tablefmt='grid'))

                            escolha= input("OPCOES [1, 2, 3, 4, 5, 0]: ")

                            try:
                                if int(escolha) == 1:
                                    time.sleep(1)
                                    print("-" * 60)
                                    print("ELENCO MASCULINO DO TIME FURIA:\n")
                                    print(tabulate(tabela_cs_masculino, headers=cabecalho_tabela_cs_times, tablefmt='grid'))
                                    print("-" * 60 + "")

                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)


                                if int(escolha) == 2:

                                    primeira_coluna = [[linha[0]] for linha in tabela_cs_masculino]
                                    nome = (tabulate(primeira_coluna, headers= ["NICK"], tablefmt='grid')).splitlines()
                                    rede_social = (tabulate(tabela_rede_social_masculino, headers=cabecalho_tabela_cs_rede, tablefmt='grid')).splitlines()

                                    time.sleep(1)
                                    print("-" * 60)
                                    print("REDES OFICIAIS DO ELENCO DA FURIA:")

                                    for tabela1, tabela2 in zip(nome, rede_social):
                                        print(f"{tabela1} {tabela2}")

                                    print("-" * 60 + "")
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)
                         
                                if int(escolha) == 3:
                                    time.sleep(1)

                                    print("-" * 60)
                                    print("CONFIGURACOES E PERIFERICOS DO ELENCO DA FURIA:\n" )
                                    print("CONFIGURACOES:\n" \
                                    "* Mouse \n" \
                                    "* Crosshair/Mira \n" \
                                    "* Viewmodel/Modelo de Visao\n" \
                                    "* Launch Option/Opcao de Inicializacao\n" \
                                    "* View Settings/Configuracoes de video\n" \
                                    "* Hud\n" \
                                    "* Radar\n" \
                                    "* Config/Configuracao\n" \
                                    "* Skins")

                                    print("\nPERIFERICOS:\n" \
                                    "* Gear/Periferico\n"\
                                    "* Pc Spec/Hardware\n"\
                                    "* Monitor Setting/Configuracao de Monitor\n")
                                    
                                    time.sleep(2)
                                    print("\nAcesse no link para visualizar os topicos mencionados:")
                                    print("-> ProSetting.net: https://prosettings.net/teams/furia/#game-468 ")
                                   
                                    print("-" * 60 + "")
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)

                                if int(escolha) == 4:

                                    trofeus_masculino = [
                                    ["Elisa Masters Espoo 2023", 2023, "1º lugar", 100000],
                                    ["IEM Rio Major 2022", 2022, "3º-4º lugar", 80000],
                                    ["ESL Pro League S12 - América do Norte", 2020, "1º lugar", 77500],
                                    ["IEM New York - America do Norte", 2020, "1º lugar", 25000],
                                    ["DreamHack Open Summer - América do Norte", 2020, "1º lugar", 25000]
                                    ]
                                
                                    tabela_masculino = tabulate(trofeus_masculino, headers=cabecalho_time_cs, tablefmt="grid")
                                    total_masculino = sum(item[3] for item in trofeus_masculino)
                                    
                                    time.sleep(1)
                                    print("-" * 60)
                                    print("PRINCIPAIS TROFEIS E PREMIACOES DA FURIA:\n")
                                    
                                    print(tabela_masculino)
                                    print(f"\nTOTAL PREMIADO (MASCULINO): US${total_masculino:,}")

                                    print("-" * 60)
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)

                                if int(escolha) == 5:
                                    time.sleep(1)
                                    print("-" * 60)
                                    print("HISTORICO DE JOGOS DA FURIA:\n" )
                                    print("Voce pode encontra-las acessando o site:\n→ Bo3.gg: https://bo3.gg/pt/teams/furia/matches ")
                                   
                                    print("-" * 60 + "")
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)

                                if int(escolha) == 0:
                                    time.sleep(0.5)   
                                    print("\nVoce escolheu retornar, um momento...\n")
                                    escolha = 99
                                    time.sleep(1)
                                    break
                            except ValueError:
                                print("\nDesculpe, nao entendi a sua escolha. TENTE NOVAMENTE...\n")
                                time.sleep(1)
                            
                            print("="*60)



                    elif int(escolha) == 2:

                        time.sleep(1)

                        print("\nCarregando informacoees do Time Feminino de COUNTER-STRIKE")
                        time.sleep(1)
                        print("Informacoes tiradas dos sites (Atualizado/Verificado ultima vez em maio):")
                        print("\n-> https://liquipedia.net/counterstrike/FURIA_Female ")
                        print("-> https://escharts.com/teams/csgo/furiafem ")
                        print("-> https://bo3.gg/teams/furia-fe ")

                        time.sleep(1.5)
                        print("="*60)

                        while True:

                            # Quarta tabela de escolhas, apresentada após escolher Counter-Strike.
                            tabela_cs_feminino = [
                                ["br kaahSENSEI(C)","Karina Takahashi","26","Jogadora"],
                                ["br bizinha ","Bruna Marvila Oliveira do Rego","25","Jogadora"],
                                ["br izaa ","Izabella Bieberbach Galle","23","Jogadora"],
                                ["br gabs ","Gabriela Freindorfer","27","Jogadora"],
                                ["ar lulitenz ","Lucia Dubra","22","Jogadora"],
                                ["(SAIDA EM 23/03/25)br Jnt ","Jhonatan Silva Moura","30","Coach"]
                             ]
                            tabela_rede_social_feminino = [
                            ["https://www.instagram.com/kaahtak/","https://x.com/kaahtak","https://www.twitch.tv/kaah"],
                            ["https://www.instagram.com/bizinhafps/ ","https://x.com/bizinhafps ","https://www.twitch.tv/bizinha "],
                            ["https://www.instagram.com/izaa_galle/ ","https://x.com/izaa_galle ","https://www.twitch.tv/izaa "],
                            ["https://www.instagram.com/gabsfreindorfer ","https://x.com/gabsfreindorfer ","https://www.twitch.tv/gabssf "],
                            ["https://www.instagram.com/ludubra ","https://x.com/LuDubra ","https://www.twitch.tv/lulitenz "],
                            ["...", "...", "..."]
                            ]

                            print("DO QUE VOCE GOSTARIA DE SE INFORMAR?")
                            time.sleep(1)
                            print (tabulate(tabela_cs_lineups_opcoes, headers=cabecalho_tabela_cs_opcoes, tablefmt='grid'))

                            escolha= input("OPCOES [1, 2, 3, 4, 5, 0]: ")

                            try:
                                if int(escolha) == 1:
                                    time.sleep(1)
                                    print("-" * 60)
                                    print("ELENCO FEMININO DA FURIA:\n")
                                    print(tabulate(tabela_cs_feminino, headers=cabecalho_tabela_cs_times, tablefmt='grid'))
                                    print("-" * 60 + "")

                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)


                                if int(escolha) == 2:

                                    primeira_coluna = [[linha[0]] for linha in tabela_cs_feminino]
                                    nome = (tabulate(primeira_coluna, headers= ["NICK"], tablefmt='grid')).splitlines()
                                    rede_social = (tabulate(tabela_rede_social_feminino, headers=cabecalho_tabela_cs_rede, tablefmt='grid')).splitlines()

                                    time.sleep(1)
                                    print("-" * 60)
                                    print("REDES SOCIAIS DO ELENCO DA FURIA:")

                                    for tabela1, tabela2 in zip(nome, rede_social):
                                        print(f"{tabela1} {tabela2}")

                                    print("-" * 60 + "")
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)
                         
                                if int(escolha) == 3:
                                    time.sleep(1)

                                    print("-" * 60)
                                    print("CONFIGURACOES E PERIFERICOS DA FURIA:\n" )

                                    print("\nInfelizmente nao consegui achar todas as informacoes detalhadas.")
                                    print("PERIFERICOS:\n" \
                                    "* Mouse\n"\
                                    "* Mousepad\n"\
                                    "* Keybord/Teclado"\
                                    "* Headset/Fone de Ouvido\n")
                                    
                                    time.sleep(2)
                                    print("Porem essas podem ser encontradas acessando o site:")
                                    print("-> liquipedia.net: https://liquipedia.net/counterstrike/List_of_player_hardware ")
                                    print("\nPARA FICAR MAIS ATUALIZADO, procure nas redes sociais das jogadoras e/ou nas redes sociais da organizacao")
                                   
                                    print("-" * 60 + "")
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)

                                if int(escolha) == 4:

                                    trofeus_feminino = [
                                    ["ESL Impact League S7 - America do Sul", 2025, "1º lugar", 3000],
                                    ["ESL Impact League S6 Finals", 2024, "2º lugar", 20000],
                                    ["Rainhas do Clutch FERJEE", 2024, "1º lugar", 17200],
                                    ["ESL Impact Katowice", 2023, "3º lugar", 10000],
                                    ["ESL Impact League S2 Finals", 2022, "2º lugar", 25000],
                                    ]

                                    tabela_feminino = tabulate(trofeus_feminino, headers=cabecalho_time_cs, tablefmt="grid")
                                    total_feminino = sum(item[3] for item in trofeus_feminino)
                                    
                                    time.sleep(1)
                                    print("-" * 60)
                                    print("PRINCIPAIS TROFEIS E PREMIACOES DA FURIA:\n")
                                    
                                    print(tabela_feminino)
                                    print(F"\nTOTAL PREMIADO (FEMININO): US$ {total_feminino}:")

                                    print("-" * 60)
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)

                                if int(escolha) == 5:
                                    time.sleep(1)
                                    print("-" * 60)
                                    print("HISTORICOS DE JOGOS DA FURIA:\n" )
                                    print("Voce pode encontra-las acessando o site:\n→ Bo3.gg: https://bo3.gg/pt/teams/furia-fe/matches ")
                                   
                                    print("-" * 60 + "")
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)

                                if int(escolha) == 0:
                                    time.sleep(0.5)   
                                    print("\nVoce escolheu retornar, um momento...\n")
                                    escolha = 99
                                    time.sleep(1)
                                    break
                            except ValueError:
                                print("\nDesculpe, nao entendi a sua escolha. TENTE NOVAMENTE...\n")
                                time.sleep(1)
                            
                            print("="*60)

                    elif int(escolha) == 3:
                        time.sleep(1)

                        print("-" * 60)
                        print("REDES SOCIAIS DA FURIA:\n" )
                        print("INSTAGRAM @furiagg  → https://www.instagram.com/furiagg/ ")
                        print("TWITTER/X @FURIA  → https://x.com/furia")
                        print("FACEBOOK FURIA  → https://www.facebook.com/furiagg/")
                        print("-" * 60 + "")

                        espera = input("Pressione qualquer tecla para continuar: ")
                        print()
                        time.sleep(0.5)

                    elif int(escolha) == 4:
                        time.sleep(1)
                        
                        print("-" * 60)
                        print("O site oficial da FURIA Esports, furia.gg, oferece uma ampla \nvariedade de produtos de moda 'streetwear'(Moda urbana), incluindo: \n" )
                        
                        print(" * Camisetas\n" \
                        " * Moletons e Jaquetas\n" \
                        " * Calcas e Shorts\n" \
                        " * Acessorios\n" \
                        " * Colecoes e Colaboracoes\n")
                        print("Para conferir todos os produtos disponiveis e realizar compras, \nvisite a loja oficial da "
                        "FURIA em: https://www.furia.gg ")
                        print("-" * 60 + "")
                        
                        espera = input("Pressione qualquer tecla para continuar: ")
                        print()
                        time.sleep(0.5)

                    elif int(escolha) == 0:
                        time.sleep(0.5)   

                        print("\nVoce escolheu retornar, um momento...\n")
                        escolha = 99
                        time.sleep(1)
                        break

                    else:
                        print("\nDesculpe, nao entendi a sua escolha. TENTE NOVAMENTE...\n")
                        time.sleep(1)
                except ValueError:
                    print("\nDesculpe, nao entendi a sua escolha. TENTE NOVAMENTE...\n")
                    time.sleep(1)
                print("="*60)

        elif int(escolha) == 2:
            print("\nVoce escolheu a lineup de VALORANT.", end=" ")
            time.sleep(1)
            print("Infelizmente esta lineup NAO ESTA DISPONIVEL...\n")
           

        elif int(escolha) == 3:
            print("\nVoce escolheu a lineup de LEAGUE OF LEGENDS.", end=" ")
            time.sleep(1)
            print("Infelizmente esta lineup NAO ESTA DISPONIVEL...\n")
            
        elif int(escolha) == 0:
            print("\nVoce escolheu finalizar a chamada, nos vemos uma outra hora. Adeus!\n")
            break

        elif int(escolha) == 99: 
            pass

        else:
            print("\nDesculpe, nao entendi a sua escolha. TENTE NOVAMENTE...\n")

    except ValueError:
        print("\nDesculpe, nao entendi a sua escolha. TENTE NOVAMENTE...\n")
    time.sleep(1)
    print("="*60)




                                        
