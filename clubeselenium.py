from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep
from datetime import datetime

# Configurar o WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Executar sem abrir o navegador (opcional)
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    contagem = 0
    while contagem < 60 :
        # Acessar o site específico de Brasília
        driver.get("https://www.clube.fm/brasilia")
        # Exibir data e hora atual
        now = datetime.now()
        print("Data e hora inicial:", now.strftime("%d-%m-%Y %H:%M:%S"))
        sleep(30)

        # Esperar o carregamento completo da página
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        #print("Título da página:", driver.title)

        # Capturar o body do HTML
        #body_html = driver.find_element(By.TAG_NAME, "body").get_attribute("outerHTML")

        # Salvar o HTML em um arquivo
        text_1 = driver.find_element(By.CLASS_NAME, "sc-1aab1d33-4.fbUEHW").text
        text_2 = driver.find_element(By.CLASS_NAME, "sc-1aab1d33-6.gkLYzf").text
        hora = now.strftime("%d-%m-%Y / %H:%M")
        #print("Texto da classe 'sc-1aab1d33-4 fbUEHW':", text_1)
        #print("Texto da classe 'sc-1aab1d33-6 gkLYzf':", text_2)
        with open(f"clube_fm.html", "a", encoding="utf-8") as file:
            file.write(f"\nmusica:{text_1} - ")
            file.write(f"artista:{text_2} - ")
            file.write(f"Data e Hora:{hora}")
        print(f"HTML salvo em clube_fm_{now.strftime('%d-%m %H:%M')}.html")

        if text_1 == 'DISK RECAÍDA':
            print("TOCOU':", text_1)

        contagem = contagem+1
        sleep(10)

        print("Contador de iterações':", contagem)
        

    
    ## Capturar e exibir o texto das classes específicas
    #try:
    #    
    #    # Salvar os textos capturados em um arquivo
    #    with open("clube_fm_textos.txt", "w", encoding="utf-8") as file:
    #        file.write(f"Texto da classe 'sc-1aab1d33-4 fbUEHW': {text_1}\n")
    #        file.write(f"Texto da classe 'sc-1aab1d33-6 gkLYzf': {text_2}\n")
    #    print("Textos salvos em clube_fm_textos.txt")
    #    
    #except Exception as e:
    #    print("Erro ao capturar o texto das classes:", str(e))
    #
finally:
    # Fechar o navegador
    now = datetime.now()
    print("Data e hora final:", now.strftime("%d-%m-%Y %H:%M:%S"))

    driver.quit()
