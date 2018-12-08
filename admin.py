# -*- coding: utf-8 -*-
#created by: hacv4

import requests

class cores: #-> invocar cores!
    vermelho = '\033[31m'
    verde = '\033[32m'
    amarelo = '\033[33m'
    final = '\033[0;0m'

def banner(): #-> printar o banner abaixo!
    print(cores.amarelo+"""
#-#-#-#-#-#-#-#-#-#-##
admin-panel-finder   |
#-#-#-#-#-#-#-#-#-#-##
"""+cores.final)

def open_file(nome: str) -> list: #-> função para abrir e retornar linhas de um arquivo em forma de lista:
    linhas = []
    try: #-> tente o que está abaixo!
        arq = open(nome.strip(), "r")
        print(cores.verde+"Arquivo solicitado Encontrado!"+cores.final)
        for linha in arq:
            linhas.append(linha.strip())
        else:
            return linhas
    except FileNotFoundError: #-> caso o arquivo não exista! Faça...
        print(cores.vermelho+"Arquivo solicitado não Encotrado!"+cores.final)
        exit()

def verificar(lista: list, link: str, show=False) -> list: #-> função principal de verificação do site!
    link = link.strip()
    links = []
    print(cores.verde+"Verificando Dados solicitados..."+cores.final)
    if link[:3] == "www": #-> se os primeiros digitos da url for os específicados!
        print(cores.vermelho+"Dados Invalidos!"+cores.final)
        return -1
    if "http://" == link[:7] or "https://" == link[:8]: #-> se os primeiros digitos da url for os específicados!
        try: #-> tente o que está abaixo!
            test = requests.get(link)
            if(test.status_code == 200): #-> se a página solicitada está pegando!
                del test
                print(cores.verde+"Página solicitada Encontrada!"+cores.final)
                for value in lista: #-> para cada valor que estiver contido dentro da lista! Faça...
                    link_completo = str(link) + "/" + str(value)
                    reque = requests.get(link_completo)
                    if show: #-> se show == True: ou se show!
                        if(reque.status_code == 200): #-> se código da página for 200, então status: OK!
                            print(cores.verde+"link: {} --> [OK]".format(link_completo)+cores.final)
                            del reque
                            continue
                        else: #-> senão, ou seja, se o de cima for falso!
                            print(cores.vermelho+"link: {} --> [NO]".format(link_completo)+cores.final)
                            del reque
                            continue
                    if not show: #-> se "show" for falso, ou seja, se o cara não quiser ver o código rodando!
                        if(reque.status_code == 200): #-> se código da página for 200, então status: OK!
                            links.append(link_completo)
                            del reque
                        else:
                            del reque
                    else: #-> senão, ou seja, se nenhuma das condições acima for verdadeira!
                        break
                else: #-> senão, ou seja, se o laço "for" for concluído com sucesso!
                    if show: #-> se show for verdadeiro, ou seja, se o cara quiser ver a execução!
                        pass
                    if not show: #-> se o cara não quiser ver a execução!
                        return links #-> retorne a lista: "links"
        except: #-> caso tenha alguma exceção!
            print(cores.vermelho+"Houve um Problema "+cores.final + cores.amarelo+"ou a"+cores.final + cores.verde+" Execução foi Completada com Sucesso!"+cores.final)
    else: #-> senão, ou seja, se a condição escita acima for falsa!
        print(cores.vermelho+"Desculpe, dados incorretos!"+cores.final)
