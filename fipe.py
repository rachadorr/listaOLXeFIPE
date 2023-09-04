import requests
#http://deividfortuna.github.io/fipe/

#busca modelo
#https://parallelum.com.br/fipe/api/v2/{vehicleType}/brands/{brandId}/models


#busca ano
#https://parallelum.com.br/fipe/api/v2/{vehicleType}/brands/{brandId}/models/{modelId}/years

#busca informação do veiculo
#https://parallelum.com.br/fipe/api/v2/{vehicleType}/brands/{brandId}/models/{modelId}/years/{yearId}

#busca historico de preço do veiculo
#https://parallelum.com.br/fipe/api/v2/{vehicleType}/{fipeCode}/years/{yearId}/history

#busca informação do veiculo pela fipe
#https://parallelum.com.br/fipe/api/v2/{vehicleType}/{fipeCode}/years/{yearId}




import json
import ast

###BLOCO PARA FUNCIONAR O BANCO DE DADOS
from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
###FIM BLOCO PARA FUNCIONAR O BANCO DE DADOS

def leTipo(Cd_Tipo):
    x = (supabase.table('Fipe_Tipo').select("*").execute())
    x = dict(x)
    y = x['data']
    x1 = dict(y[(Cd_Tipo-1)])
    print (x1)
    return x1
    
def leMarca(Cd_Tipo):
    tipo = leTipo(Cd_Tipo)
    print(tipo)
    x = (supabase.table("Fipe_Marca").select("*").eq("Cd_Tipo",f'{tipo["id"]}').order("Cd_Fipe", desc=False).execute())
    x = dict(x)
    y = x['data']
    #print (y)
    return y

def carregaMarcas(tipo):
    tipo = leTipo(tipo)
    #print(type(tipo))
    #print(tipo['id'])
    #print(tipo['Tipo'])
    request = requests.get(f"http://parallelum.com.br/fipe/api/v2/{tipo['Tipo']}/brands")
    todos = json.loads(request.content)
    ##print(todos)
    for i in range(len(todos)):
    ####    print(i)
        supabase.table('Fipe_Marca').insert({"Marca":(todos[i]["name"]), "Cd_Fipe":(todos[i]["code"]),"Cd_Tipo":(tipo['id'])}).execute()
    #    #print(todos[i]["name"])

def carregaModelo(tipo, marca):
    tipo = leTipo(tipo)
    marca = leMarca(tipo['id'])
    #print (marca)
    x1 = dict(marca)
    print (x1)
    #print (f"https://parallelum.com.br/fipe/api/v2/{tipo['Tipo']}/brands/{marca['Cd_Fipe']}/models")
    #print (marca)
    #request = requests.get(f"https://parallelum.com.br/fipe/api/v2/{tipo['Tipo']}/brands/{marca['Cd_Fipe']}/models")
    #todos = json.loads(request.content)
    ###print(todos)
    #for i in range(len(todos)):
    #####    print(i)
    #    supabase.table('Fipe_Marca').insert({"Marca":(todos[i]["name"]), "Cd_Fipe":(todos[i]["code"]),"Cd_Tipo":(tipo['id'])}).execute()
    ##    #print(todos[i]["name"])

#leTipo(1)
#leModelo(1)
carregaModelo(1,1)