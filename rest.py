import requests

def consult():
    response = requests.get('http://127.0.0.1:8090/treinador/')
    print(response.status_code)
    print(response.json()) 
    for treinador in response.json():
        print(treinador['id'], treinador['nome'], treinador['pokemon'])
        
def insert():
    nome = 'Star'
    pokemon = 'Celebi'
    treinador = {"nome": nome,"pokemon": pokemon}
    response = requests.post('http://127.0.0.1:8090/treinador/', json=treinador)
    print(response.status_code)
    print(response.json()) 
    
insert()
consult()

      