import json

pessoas = [
    {'nome': 'Bruno', 'telefone': '(83)98821-2312', 'endereco': 'ABC'},
    {'nome': 'Aline', 'telefone': '(83)98200-2341', 'endereco': 'DDD'},
    {'nome': 'John', 'telefone': '(83)98121-2000', 'endereco': 'GEC'},
]

with open('pessoas.json', 'w') as arquivos:
    json.dump(pessoas, arquivos, indent=4)