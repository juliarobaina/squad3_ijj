from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #para simular teclas do teclado e preencher campos
from selenium.webdriver.support.ui import Select #para usar com a tag select

import time

browser = Firefox()

link = "https://www.google.com/"

browser.get(link)

btnSearch = browser.find_element(By.ID, "APjFqb")
btnSearch.send_keys("Instituto Joga Junto",Keys.ENTER)
# search Waits in selenium
time.sleep(3)

totalCite = browser.find_elements(By.TAG_NAME,"cite")

for cite in totalCite:
    if cite.text == "https://jogajuntoinstituto.org":
        cite.click()
        break # se não tiver break fica em loop infinito

form = browser.find_element(By.TAG_NAME, "form")

inputName = form.find_element(By.NAME,"nome")
inputName.send_keys("Teste Atividade Módulo Avançado")

inputEmail = form.find_element(By.NAME,"email")
inputEmail.send_keys("testeatividademoduloavancado@gmail.com")

#recebe o elemento select com nome assunto
select = Select(browser.find_element(By.NAME, 'assunto'))
#seleciona o option que está com essa mensagem sendo exibida para o usuário na tela
select.select_by_visible_text("Me inscrever em um curso")

textarea = form.find_element(By.NAME, "body").send_keys("Teste Atividade Joga Junto")

#envia o formulário
form.submit()

time.sleep(10)
browser.quit()