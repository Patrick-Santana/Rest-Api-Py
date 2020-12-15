import requests

def consult():
    response = requests.get('http://127.0.0.1:8090/pessoa/')
    print(response.status_code)
    print(response.json()) 
    for pessoa in response.json():
        print(pessoa['id'], pessoa['nome'], pessoa['pokemon'])
        
def insert():
    nome = 'Sandro'
    pokemon = 'Snorlax'
    pessoa = {"nome": nome,"pokemon": pokemon}
    response = requests.post('http://127.0.0.1:8090/pessoa/', json=pessoa)
    print(response.status_code)
    print(response.json()) 
    
insert()
consult()