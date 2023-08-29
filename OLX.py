import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep


site= 'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-rs?sf=1&o=1'
#'https://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/autos-e-pecas/carros-vans-e-utilitarios/virtus-200tsi-confortline-2022-2022-unica-dona-1187757332?lis=listing_2020'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = requests.get(site, headers=hdr)
#req = requests.get(site,headers=hdr)
#page = urlopen(req.text)
print(req.status_code)
site = BeautifulSoup(req.text,"html.parser")
#site = BeautifulSoup(req.text,"html5lib") #teste com html5lib

# arquivo que armazena o site para testes
f = open("teste.txt", "a")
f.write(site.prettify())
print(type(site))

#pesquisa = site.find_all("div",class_="sc-bb3a36b6-0 bPPSiI renderIfVisible")
pesquisa = site.find_all("div",class_="sc-bb3a36b6-0 bPPSiI renderIfVisible")
print(len(pesquisa))

for th in pesquisa:
    sleep(2)
    #print(th.find_all("div",class_="sc-giYglK iODuKY horizontal"))
    v = th.find("a",class_="sc-dJjYzT dOvWTZ")
    try:
        #print (th)
        print (f"teste: {v['href']}")
    except TypeError as e:
        print(e)
        print("handled successfully")


    #print (th.text)

#veiculo1 = veiculo.find_all("img")
#print(result[0])

#print(site.prettify())

#print(req.text)


