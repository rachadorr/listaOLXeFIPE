from typing_extensions import Concatenate
import requests
from time import sleep


file_url = 'https://cdn-selpics.youfocus.com.br/gallery/1691588090-64d395fa490e91167438219.jpg'

#file = 'foto1.jpg'

#r = requests.get(file_url) 
#with open("python_logo.png",'wb') as f: 
#    f.write(r.content) 




# list de a-n
#for i in range(ord('a'), ord('e')+1):
#    lista[62] = chr(i)
#    frase = "".join(lista)
#    #print(f"Esse é a frase incluindo o caracter: {frase}")
#    for i in range(ord('0'), ord('9')+1):
#        lista[63] = chr(i)
#        frase = "".join(lista)
#        for i in range(ord('a'), ord('d')+1):
#            lista[63] = chr(i)
#            frase = "".join(lista)
#            for i in range(ord('a'), ord('f')+1):
#                lista[64] = chr(i)
#                frase = "".join(lista)
#                for i in range(ord('0'), ord('9')+1):
#                    lista[64] = chr(i)
#                    frase = "".join(lista)
#                    r = requests.get(frase)
#                    print(f"Baixando: {frase}")
#                    sleep(2)
#
#                    with open(frase[-38:],'wb') as f: 
#                        f.write(r.content) 

def atualizaNome(indice, lista):
    for i in range(ord('a'), ord('z')+1):
        lista[indice] = chr(i)
        frase = "".join(lista)
        print(frase)
    #print("pulou")
        #print(f"Esse é a frase incluindo o caracter: {frase}")
    for i in range(ord('0'), ord('9')+1):
        lista[indice] = chr(i)
        frase = "".join(lista)
        print(frase)

    
             
a =[]
#for i in range(64, len(file_url)-3):
for i in range(63, len(file_url)-4):
    print (f"indice{i}")
    atualizaNome(i,list(file_url))
#

#for i in range(ord('0'), ord('9')):
#    a.append (chr(i))
#
#print(len(file_url))
#
#for i in range( 64, len(file_url)-3):
#    print(i)
#        
#print(list(range(5)))
#
#print(a)

      
      
      
      
    #frase = frase[:-6]
 #   print(f"Esse é a frase depois de excluir o caracter: {frase}")

#print(a)
#print(frase)
