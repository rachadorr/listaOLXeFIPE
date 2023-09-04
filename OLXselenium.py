from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)



service = Service(ChromeDriverManager().install())
#
options = webdriver.ChromeOptions()
#
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#data = supabase.table('Veiculo').select("*").execute()
#print(type(data))
#print(data)
#carro = 'https://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/autos-e-pecas/carros-vans-e-utilitarios/tracker-lt-1-0-turbo-22-23-1215981091'
#carro = carro.split("/")[-1]
#print (carro)
#print (carro.split("-")[-1])



nav = webdriver.Chrome(service=service,options=options)
nav.maximize_window() 

nav.get('https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-rs?sf=1&o=1')
print("Carregou a pagina e espera 4 segundos")
sleep(4)
print("Carregou a pagina e esperou 4 segundos")
lista = []
def leCarros():
        for i in range(3,55+1):
            try:
                nav.execute_script("window.scrollBy(0,270)","")
                sleep(3)
                #print("Carregou a pagina e esperou 3 segundos")
                url = '//*[@id="main-content"]/div['+str(i)+']/section/a'
                #print(f'Carregou essa URL: {url}')
                sleep(2)
                req = nav.find_element(By.XPATH, url)
                v = (req.get_attribute("href"))
                #print('passou')
                print(f'Carregou essa carro: {v}')
                supabase.table('Veiculo').insert({"veiculo":(v.split("/")[-1]),"codigo":(v.split("-")[-1]), "link":(v)}).execute()
                lista.append(v)
            except:
                None
#print(lista)

for i in range(1,3):
    nav.get('https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-rs?sf=1&o='+str(i)+'')
    print("Carregou a pagina e espera 4 segundos")
    sleep(4)
    print("Carregou a pagina e esperou 4 segundos")
    #nav.maximize_window() 
    leCarros()
#
print("Buscou o elemento")
print(lista)
#print(req.get_attribute("outerHTML"))
#print(req.get_attribute("href"))
#for element in req:
#    print(element.get_attribute("outerHTML"))
#    print(element.get_attribute("href"))
#    #print(element)
    

#site= 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-rs?sf=1&o=1'
##'https://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/autos-e-pecas/carros-vans-e-utilitarios/virtus-200tsi-confortline-2022-2022-unica-dona-1187757332?lis=listing_2020'
#hdr = {'User-Agent': 'Mozilla/5.0'}
#req = requests.get(site, headers=hdr)
##req = requests.get(site,headers=hdr)
##page = urlopen(req.text)
#print(req.status_code)
#site = BeautifulSoup(req.text,"html.parser")
##site = BeautifulSoup(req.text,"html5lib") #teste com html5lib
#
## arquivo que armazena o site para testes
#f = open("teste.txt", "a")
#f.write(site.prettify())
#print(type(site))
#
##pesquisa = site.find_all("div",class_="sc-bb3a36b6-0 bPPSiI renderIfVisible")
#pesquisa = site.find_all("div",class_="sc-bb3a36b6-0 bPPSiI renderIfVisible")
#print(len(pesquisa))
#
#for th in pesquisa:
#    sleep(2)
#    #print(th.find_all("div",class_="sc-giYglK iODuKY horizontal"))
#    v = th.find("a",class_="sc-dJjYzT dOvWTZ")
#    try:
#        #print (th)
#        print (f"teste: {v['href']}")
#    except TypeError as e:
#        print(e)
#        print("handled successfully")
#
#
#    #print (th.text)
#
##veiculo1 = veiculo.find_all("img")
##print(result[0])
#
##print(site.prettify())
#
##print(req.text)
#
#
#