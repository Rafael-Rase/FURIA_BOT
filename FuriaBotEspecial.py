from tabulate import tabulate
import time

# -*- coding: utf-8 -*-

#variaveis para modificar os print (deixar mais claro)
negrito = "\033[1m"
azul_sublinhado = "\033[34;4m"
padrao = "\033[0m"


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
print(f"🐾 OLA, BEM-VINDO AO CHAT {negrito}FEITO PARA FÃS FURIOSOS!{padrao}")
print(f"Este chat é feito para mostrar informações relevantes sobres as \n{negrito}principais lineups da FURIA{padrao}")
time.sleep(1)

# Tabela inicial de escolhas de modalidades de e-sports da FURIA.
tabela_lineup = [
    ["1- Counter-Strike","Jogo de tiro tático","Disponível"],
    ["2- Valorant","Jogo de tiro tático", "Indisponível"],
    ["3- League of Legends","Moba", "Indisponível"],
    ["0- ❌ Sair"]
] 

cabecalho_tabela_lineup = [f"{negrito}LINEUPS","GÊNERO",f"ACESSO{padrao}"]
cabecalho_tabela_opcoes = [f"{negrito}OPÇÃO{padrao}"]
escolha = 1

print("\nPARA COMEÇAR,", end=" ")

# Primeiro laço de repetição (loop principal do programa).
while True:
    print(f"ESCOLHA UMA OPÇÃO") 
    time.sleep(1)

   
    print (tabulate(tabela_lineup[0:3], headers=cabecalho_tabela_lineup, tablefmt='grid'), )
    print (tabulate(tabela_lineup[3:], headers=cabecalho_tabela_opcoes, tablefmt='grid'))

    #Esperando resposta
    escolha = input(f"LINEUP [1, 2, 3, 0]: ") 
    
    # Uso do bloco "try" para lidar com possíveis erros se o usuário inserir um valor não inteiro.
    try:
        if int(escolha) == 1:
            print(f" \nVoce escolheu a lineup de {negrito}COUNTER-STRIKE{padrao}.", end= " ")
            time.sleep(1)
            print("ESTA DISPONÍVEL!\nVamos prosseguir...\n")          
            time.sleep(1)

            # Tabela secundária de escolhas, apresentada após o usuário escolher Counter-Strike.
            tabela_cs_lineup = [
                ["1- 🐾 Furia Masculino"], 
                ["2- 🐾 Furia Feminino"],
                ["3- 🌐 Redes Sociais"],
                ["4- 📱 Loja Virtual"],
                ["0- 🔙 Voltar"]
            ]
            
            cabecalho_tabela_cs_lineup = [f"{negrito}LINEUP{padrao}"]
            cabecalho_tabela_cs_opcoes = [f"{negrito}OPÇÕES{padrao}"]           

            print("="*60)

            # Segundo laço de repetição (loop para as opções de Counter-Strike).
            while True:

                # Terceira tabela de escolhas, apresentada após escolher Counter-Strike.
                tabela_cs_lineups_opcoes = [
                                ["1- 👥 Elenco"],
                                [f"2- 🌐 Redes Sociais {negrito}(link){padrao}"],
                                [f"3- 🖱️ Configurações e Periféricos {negrito}(link){padrao}"],
                                ["4- 🏆 Troféis e Premiações"],
                                [f"5- 📜 Ultimos Jogos {negrito}(link){padrao}"],
                                ["0- 🔙 Voltar"]
                            ]
           
                cabecalho_tabela_cs_times = [f"{negrito}NICK", "NOME", "IDADE",f"POSIÇÃO{padrao}"]
                cabecalho_tabela_cs_rede = [f"{negrito}X/TWITTER","INSTAGRAM",f"TWITCH{padrao}"]
                cabecalho_time_cs = [f"{negrito}Campeonato", "Ano", "Colocação", f"Premiação (US$){padrao}"]

                print("DO QUE VOCE GOSTARIA DE SE INFORMAR?")
                time.sleep(1)

             
                print (tabulate(tabela_cs_lineup[0:2], headers=cabecalho_tabela_cs_lineup, tablefmt='grid'))
                print (tabulate(tabela_cs_lineup[2:5], headers=cabecalho_tabela_cs_opcoes, tablefmt='grid'))
                escolha= input("OPÇÕES [1, 2, 3, 4, 0]: ") 
                try:
                    if int(escolha) == 1:
                        time.sleep(1)

                        
                        print(f"\nCarregando informaçõees do {negrito}Time Masculino de COUNTER-STRIKE{padrao}")
                        time.sleep(1)
                        print(f"Informações tiradas dos sites ({negrito}Atualizado/Verificado ultima vez em maio{padrao}):")
                        print(f"\n{azul_sublinhado}→ https://www.hltv.org/team/8297/furia {padrao}")
                        print(f"{azul_sublinhado}→ https://prosettings.net/teams/furia/#game-468 {padrao}")
                        print(f"{azul_sublinhado}→ https://bo3.gg/teams/furia {padrao}\n")

                        time.sleep(1.5)
                        print("="*60)

                        # Terceiro laço de repetição (loop para as opções do time masculino).
                        while True:
                           
                 
                            tabela_cs_masculino = [
                                ["🇧🇷 FalleN👑","Gabriel Toledo","33","Jogador"],
                                ["🇧🇷 yuurih ","Yuri Santos ","25","Jogador "],
                                ["🇱🇻 YEKINDAR ","Mareks Gaļinskis ","25","Jogador "],
                                ["🇧🇷 KSCERATO ","Kaike Cerato ","25","Jogador "],
                                ["🇰🇿 molodoy ","Danil Golubenko ","20","Jogador "],
                                ["🇧🇷 sidde "," Sid Macedo ","28","Coach "]
                            ]
                            
                            tabela_rede_social_masculino = [
                                [f"{azul_sublinhado}x.com/i/user/112897001{padrao}",f"{azul_sublinhado}https://www.instagram.com/fallen{padrao}",f"{azul_sublinhado}https://www.twitch.tv/gafallen{padrao}"],
                                [f"{azul_sublinhado}https://x.com/yuurih {padrao}",f"{azul_sublinhado}https://www.instagram.com/yuurihfps {padrao}"],
                                [f"{azul_sublinhado}https://x.com/yek1ndar {padrao}",f"{azul_sublinhado}https://www.instagram.com/yek1ndar {padrao}",f"{azul_sublinhado}https://www.twitch.tv/yekindar {padrao}"],
                                [f"{azul_sublinhado}https://x.com/kscerato {padrao}",f"{azul_sublinhado}https://www.instagram.com/kscerato {padrao}"],
                                [f"{azul_sublinhado}https://x.com/tvoy_molodoy {padrao}"],
                                [f"{azul_sublinhado}https://x.com/siddecs {padrao}",f"{azul_sublinhado}https://www.instagram.com/siddecs/ {padrao}"],
                                
                             ]
                            
                            print("DO QUE VOCE GOSTARIA DE SE INFORMAR?")
                            time.sleep(1)
                            print (tabulate(tabela_cs_lineups_opcoes, headers=cabecalho_tabela_cs_opcoes, tablefmt='grid'))

                            escolha= input("OPÇÕES [1, 2, 3, 4, 5, 0]: ")

                            try:
                                if int(escolha) == 1:
                                    time.sleep(1)
                                    print("-" * 60)
                                    print(f"👥 {negrito}Elenco masculino da FURIA:{padrao}\n")
                                    print(tabulate(tabela_cs_masculino, headers=cabecalho_tabela_cs_times, tablefmt='grid'))
                                    print("-" * 60 + "")

                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)


                                if int(escolha) == 2:

                                    primeira_coluna = [[linha[0]] for linha in tabela_cs_masculino]
                                    nome = (tabulate(primeira_coluna, headers= [f"{negrito}NICK{padrao}"], tablefmt='grid')).splitlines()
                                    rede_social = (tabulate(tabela_rede_social_masculino, headers=cabecalho_tabela_cs_rede, tablefmt='grid')).splitlines()

                                    time.sleep(1)
                                    print("-" * 60)
                                    print(f"🌐 {negrito}Redes Sociais Oficiais do Elenco da FURIA:{padrao}")

                                    for tabela1, tabela2 in zip(nome, rede_social):
                                        print(f"{tabela1} {tabela2}")

                                    print("-" * 60 + "")
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)
                         
                                if int(escolha) == 3:
                                    time.sleep(1)

                                    print("-" * 60)
                                    print(f"🖱️ {negrito}Configurações e Periféricos do Elenco da FURIA:{padrao}\n" )
                                    print(f"{negrito} Configuracoes:{padrao}\n" \
                                    "* Mouse \n" \
                                    "* Crosshair/Mira \n" \
                                    "* Viewmodel/Modelo de Visão\n" \
                                    "* Launch Option/Opção de Inicialização\n" \
                                    "* View Settings/Configurações de vídeo\n" \
                                    "* Hud\n" \
                                    "* Radar\n" \
                                    "* Config/Configuração\n" \
                                    "* Skins")

                                    print(f"\n{negrito} Periféricos:{padrao}\n" \
                                    "* Gear/Periférico\n"\
                                    "* Pc Spec/Hardware\n"\
                                    "* Monitor Setting/Configuração de Monitor\n")
                                    
                                    time.sleep(2)
                                    print("\nAcesse no link para visualizar os tópicos mencionados:")
                                    print(f"→ {negrito}ProSetting.net{padrao}: {azul_sublinhado}https://prosettings.net/teams/furia/#game-468 {padrao}")
                                   
                                    print("-" * 60 + "")
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)

                                if int(escolha) == 4:

                                    trofeus_masculino = [
                                    ["Elisa Masters Espoo 2023", 2023, "1º lugar", 100000],
                                    ["IEM Rio Major 2022", 2022, "3º-4º lugar", 80000],
                                    ["ESL Pro League S12 - América do Norte", 2020, "1º lugar", 77500],
                                    ["IEM New York - América do Norte", 2020, "1º lugar", 25000],
                                    ["DreamHack Open Summer - América do Norte", 2020, "1º lugar", 25000]
                                    ]
                                
                                    tabela_masculino = tabulate(trofeus_masculino, headers=cabecalho_time_cs, tablefmt="grid")
                                    total_masculino = sum(item[3] for item in trofeus_masculino)
                                    
                                    time.sleep(1)
                                    print("-" * 60)
                                    print(f"🏆 {negrito}Principais Troféis e Premiações da FURIA:{padrao}\n")
                                    
                                    print(tabela_masculino)
                                    print(f"\n💰 TOTAL PREMIADO (MASCULINO): US${total_masculino:,}")

                                    print("-" * 60)
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)

                                if int(escolha) == 5:
                                    time.sleep(1)
                                    print("-" * 60)
                                    print(f"📜 {negrito}Histórico de jogos da FURIA:{padrao}\n" )
                                    print(f"Voce pode encontrá-las acessando o site:\n→ {negrito}Bo3.gg{padrao}: {azul_sublinhado}https://bo3.gg/pt/teams/furia/matches {padrao}")
                                   
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
                                print("\nDesculpe, não entendi a sua escolha. TENTE NOVAMENTE...\n")
                                time.sleep(1)
                            
                            print("="*60)



                    elif int(escolha) == 2:

                        time.sleep(1)

                        print(f"\nCarregando informaçõees do {negrito}Time Feminino de COUNTER-STRIKE{padrao}")
                        time.sleep(1)
                        print(f"Informações tiradas dos sites ({negrito}Atualizado/Verificado ultima vez em maio{padrao}):")
                        print(f"\n{azul_sublinhado}→ https://liquipedia.net/counterstrike/FURIA_Female {padrao}")
                        print(f"{azul_sublinhado}→ https://escharts.com/teams/csgo/furiafem {padrao}")
                        print(f"{azul_sublinhado}→ https://bo3.gg/teams/furia-fe {padrao}")

                        time.sleep(1.5)
                        print("="*60)

                        while True:

                            # Quarta tabela de escolhas, apresentada após escolher Counter-Strike.
                            tabela_cs_feminino = [
                                ["🇧🇷 kaahSENSEI👑","Karina Takahashi","26","Jogadora"],
                                ["🇧🇷 bizinha ","Bruna Marvila Oliveira do Rego ","25 ","Jogadora "],
                                ["🇧🇷 izaa ","Izabella Bieberbach Galle ","23","Jogadora "],
                                ["🇧🇷 gabs ","Gabriela Freindorfer ","27","Jogadora "],
                                ["🇦🇷 lulitenz ","Lucia Dubra ","22","Jogadora "],
                                [f"{negrito}(SAÍDA EM 23/03/25){padrao}🇧🇷 Jnt ","Jhonatan Silva Moura ","30 ","Coach "]
                             ]
                            tabela_rede_social_feminino = [
                            [f"{azul_sublinhado}https://www.instagram.com/kaahtak/{padrao}",f"{azul_sublinhado}https://x.com/kaahtak{padrao}",f"{azul_sublinhado}https://www.twitch.tv/kaah{padrao}"],
                            [f"{azul_sublinhado}https://www.instagram.com/bizinhafps/ {padrao}",f"{azul_sublinhado}https://x.com/bizinhafps {padrao}",f"{azul_sublinhado}https://www.twitch.tv/bizinha {padrao}"],
                            [f"{azul_sublinhado}https://www.instagram.com/izaa_galle/ {padrao}",f"{azul_sublinhado}https://x.com/izaa_galle {padrao}",f"{azul_sublinhado}https://www.twitch.tv/izaa {padrao}"],
                            [f"{azul_sublinhado}https://www.instagram.com/gabsfreindorfer {padrao}",f"{azul_sublinhado}https://x.com/gabsfreindorfer {padrao}",f"{azul_sublinhado}https://www.twitch.tv/gabssf {padrao}"],
                            [f"{azul_sublinhado}https://www.instagram.com/ludubra {padrao}",f"{azul_sublinhado}https://x.com/LuDubra {padrao}",f"{azul_sublinhado}https://www.twitch.tv/lulitenz {padrao}"],
                            ["...", "...", "..."]
                            ]

                            print("DO QUE VOCE GOSTARIA DE SE INFORMAR?")
                            time.sleep(1)
                            print (tabulate(tabela_cs_lineups_opcoes, headers=cabecalho_tabela_cs_opcoes, tablefmt='grid'))

                            escolha= input("OPÇÕES [1, 2, 3, 4, 5, 0]: ")

                            try:
                                if int(escolha) == 1:
                                    time.sleep(1)
                                    print("-" * 60)
                                    print(f"👥 {negrito}Elenco feminino da FURIA:{padrao}\n")
                                    print(tabulate(tabela_cs_feminino, headers=cabecalho_tabela_cs_times, tablefmt='grid'))
                                    print("-" * 60 + "")

                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)


                                if int(escolha) == 2:

                                    primeira_coluna = [[linha[0]] for linha in tabela_cs_feminino]
                                    nome = (tabulate(primeira_coluna, headers= [f"{negrito}NICK{padrao}"], tablefmt='grid')).splitlines()
                                    rede_social = (tabulate(tabela_rede_social_feminino, headers=cabecalho_tabela_cs_rede, tablefmt='grid')).splitlines()

                                    time.sleep(1)
                                    print("-" * 60)
                                    print(f"🌐 {negrito}Redes Sociais Oficiais do Elenco da FURIA:{padrao}")

                                    for tabela1, tabela2 in zip(nome, rede_social):
                                        print(f"{tabela1} {tabela2}")

                                    print("-" * 60 + "")
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)
                         
                                if int(escolha) == 3:
                                    time.sleep(1)

                                    print("-" * 60)
                                    print(f"🖱️ {negrito}Configurações e Periféricos do Elenco da FURIA:{padrao}\n" )

                                    print("\nInfelizmente não consegui achar todas as informações detalhadas.")
                                    print(f"{negrito} Periféricos:{padrao}\n" \
                                    "* Mouse\n"\
                                    "* Mousepad\n"\
                                    "* Keybord/Teclado"\
                                    "* Headset/Fone de Ouvido\n")
                                    
                                    time.sleep(2)
                                    print("Porem essas podem ser encontradas acessando o site:")
                                    print(f"→ {negrito}liquipedia.net{padrao}: {azul_sublinhado}https://liquipedia.net/counterstrike/List_of_player_hardware {padrao}")
                                    print(f"\n{negrito}Para ficar mais atualizado, procure nas redes sociais das jogadoras e/ou nas redes sociais da organização{padrao}")
                                   
                                    print("-" * 60 + "")
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)

                                if int(escolha) == 4:

                                    trofeus_feminino = [
                                    ["ESL Impact League S7 - América do Sul", 2025, "1º lugar", 3000],
                                    ["ESL Impact League S6 Finals", 2024, "2º lugar", 20000],
                                    ["Rainhas do Clutch FERJEE", 2024, "1º lugar", 17200],
                                    ["ESL Impact Katowice", 2023, "3º lugar", 10000],
                                    ["ESL Impact League S2 Finals", 2022, "2º lugar", 25000],
                                    ]

                                    tabela_feminino = tabulate(trofeus_feminino, headers=cabecalho_time_cs, tablefmt="grid")
                                    total_feminino = sum(item[3] for item in trofeus_feminino)
                                    
                                    time.sleep(1)
                                    print("-" * 60)
                                    print(f"🏆 {negrito}Principais Troféis e Premiações da FURIA:{padrao}\n")
                                    
                                    print(tabela_feminino)
                                    print(f"\n💰 TOTAL PREMIADO (FEMININO): US${total_feminino:,}")

                                    print("-" * 60)
                                    espera = input("Pressione qualquer tecla para continuar: ")
                                    print()
                                    time.sleep(0.5)

                                if int(escolha) == 5:
                                    time.sleep(1)
                                    print("-" * 60)
                                    print(f"📜 {negrito}Histórico de jogos da FURIA:{padrao}\n" )
                                    print(f"Voce pode encontrá-las acessando o site:\n→ {negrito}Bo3.gg{padrao}: {azul_sublinhado}https://bo3.gg/pt/teams/furia-fe/matches {padrao}")
                                   
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
                                print("\nDesculpe, não entendi a sua escolha. TENTE NOVAMENTE...\n")
                                time.sleep(1)
                            
                            print("="*60)

                    elif int(escolha) == 3:
                        time.sleep(1)

                        print("-" * 60)
                        print(f"🌐 {negrito}Redes Sociais Oficiais da FURIA:{padrao}\n" )
                        print(f"{negrito}Instagram{padrao} @furiagg  → {azul_sublinhado}https://www.instagram.com/furiagg/ {padrao}")
                        print(f"{negrito}Twitter/X{padrao} @FURIA  → {azul_sublinhado}https://x.com/furia {padrao}")
                        print(f"{negrito}Facebook{padrao} FURIA  → {azul_sublinhado}https://www.facebook.com/furiagg/ {padrao}")
                        print("-" * 60 + "")

                        espera = input("Pressione qualquer tecla para continuar: ")
                        print()
                        time.sleep(0.5)

                    elif int(escolha) == 4:
                        time.sleep(1)
                        
                        print("-" * 60)
                        print("🌐 O site oficial da FURIA Esports, furia.gg, oferece uma ampla \nvariedade de produtos de moda 'streetwear'(Moda urbana), incluindo: \n" )
                        
                        print(f"{negrito} * Camisetas\n" \
                        " * Moletons e Jaquetas\n" \
                        " * Calças e Shorts\n" \
                        " * Acessórios\n" \
                        f" * Coleções e Colaborações{padrao}\n")
                        print("Para conferir todos os produtos disponíveis e realizar compras, \nvisite a loja oficial da "
                        f"FURIA em:\n{azul_sublinhado}https://www.furia.gg {padrao}")
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
                        print("\nDesculpe, não entendi a sua escolha. TENTE NOVAMENTE...\n")
                        time.sleep(1)
                except ValueError:
                    print("\nDesculpe, não entendi a sua escolha. TENTE NOVAMENTE...\n")
                    time.sleep(1)
                print("="*60)

        elif int(escolha) == 2:
            print(f"\nVoce escolheu a lineup de {negrito}VALORANT{padrao}.", end=" ")
            time.sleep(1)
            print("Infelizmente esta lineup NÃO ESTA DISPONÍVEL...\n")
           

        elif int(escolha) == 3:
            print(f"\nVoce escolheu a lineup de {negrito}LEAGUE OF LEGENDS{padrao}.", end=" ")
            time.sleep(1)
            print("Infelizmente esta lineup NÃO ESTA DISPONÍVEL...\n")
            
        elif int(escolha) == 0:
            print("\nVoce escolheu finalizar a chamada, nos vemos uma outra hora. Adeus!\n")
            break

        elif int(escolha) == 99: 
            pass

        else:
            print("\nDesculpe, não entendi a sua escolha. TENTE NOVAMENTE...\n")

    except ValueError:
        print("\nDesculpe, não entendi a sua escolha. TENTE NOVAMENTE...\n")
    time.sleep(1)
    print("="*60)




                                        
