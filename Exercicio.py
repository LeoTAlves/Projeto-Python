"""
Crie um programa que simule um sistema simples de acesso a uma festa.
Objetivo
O programa deve pedir ao usuário:
Nome
Idade
Se possui convite (sim ou não)
"""
nome = (input("Qual é o seu nome?:"))
idade = int(input("Qual é a sua idade?:"))
convite = (input("possui convite? (sim) ou (não):"))

"""Regras
Se a pessoa tiver 18 anos ou mais E possuir convite:
Mostrar:
Entrada permitida. Bem-vindo(a)!
Se tiver 18 anos ou mais, mas não possuir convite:
Mostrar:
Entrada negada. Você precisa de um convite.
Se for menor de idade:
Mostrar:
Entrada proibida para menores de idade.
"""
if idade >= 18 and convite == "sim":
    print("Entrada permitida, Seja bem vindo e boa festa.")

elif idade >= 18 and convite == "não":
    print("Entrada negada, convite obrigatório.")

else:
    print("Entrada negada para menores de idade.")