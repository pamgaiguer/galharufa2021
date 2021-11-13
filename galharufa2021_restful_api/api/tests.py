import requests
from pprint import pprint

# API tests

URL = "http://127.0.0.1:8000/api/"

# Non-admin URLs


def getAtores():
    # GET atores/

    print("\nGET atores/\n")
    r = requests.get(f"{URL}atores/")
    response = r.json()
    for json in response:
        print("\n*********************\n")
        pprint(json)
        print("\n*********************\n")


def getFiguracoes():
    # GET figuracoes/

    print("\nGET figuracoes/\n")
    r = requests.get(f"{URL}figuracoes/")
    response = r.json()
    for json in response:
        print("\n*********************\n")
        pprint(json)
        print("\n*********************\n")


def getModelosMasculinos():
    # GET modelos-masculinos/

    print("\nGET modelos-masculinos/\n")
    r = requests.get(f"{URL}modelos-masculinos/")
    response = r.json()
    for json in response:
        print("\n*********************\n")
        pprint(json)
        print("\n*********************\n")


def getModelosFemininos():
    # GET modelos-femininos

    print("\nGET modelos-femininos\n")
    r = requests.get(f"{URL}modelos-femininos/")
    response = r.json()
    for json in response:
        print("\n*********************\n")
        pprint(json)
        print("\n*********************\n")


def getCriancas():
    # GET criancas/

    print("\nGET criancas/\n")
    r = requests.get(f"{URL}criancas/")
    response = r.json()
    for json in response:
        print("\n*********************\n")
        pprint(json)
        print("\n*********************\n")


def getAtor(slug):
    # GET ator/<slug:slug>/

    print("\nGET ator/<slug:slug>/\n")
    r = requests.get(f"{URL}ator/{slug}")
    response = r.json()
    pprint(response)
    print("\n*********************\n")


def getFiguracao(slug):
    # GET figuracao/<slug:slug>/

    print("\nGET figuracao/<slug:slug>/\n")
    r = requests.get(f"{URL}figuracao/{slug}")
    response = r.json()
    pprint(response)
    print("\n*********************\n")


def getModeloMasculino(slug):
    # GET modelo-masculino/<slug:slug>/

    print("\nGET modelo-masculino/<slug:slug>/\n")
    r = requests.get(f"{URL}modelo-masculino/{slug}")
    response = r.json()
    pprint(response)
    print("\n*********************\n")


def getModeloFeminino(slug):
    # GET modelo-feminino/<slug:slug>/

    print("\nGET modelo-feminino/<slug:slug>/\n")
    r = requests.get(f"{URL}modelo-feminino/{slug}")
    response = r.json()
    pprint(response)
    print("\n*********************\n")


def getCrianca(slug):
    # GET crianca/<slug:slug>/

    print("\nGET crianca/<slug:slug>/\n")
    r = requests.get(f"{URL}crianca/{slug}")
    response = r.json()
    pprint(response)
    print("\n*********************\n")


# Admin URLs


def getPessoas(key):
    # GET pessoas-admin/

    headers = {"Authorization": f"Bearer {key}",
               "Content-type": "application/json"}

    print("\nGET pessoas-admin/\n")
    r = requests.get(url=f"{URL}atores/", headers=headers)
    response = r.json()
    for json in response:
        print("\n*********************\n")
        pprint(json)
        print("\n*********************\n")
