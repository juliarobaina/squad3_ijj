from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

import time

#cria uma instância de Firefox
browser = Firefox()

link = "https://page-test-selenium.s3.sa-east-1.amazonaws.com/index.html"

#carrega uma página pela url com o método get
browser.get(link)

#captura o elemento html de id addElement (captura um elemento)
btnAddElement = browser.find_element(By.ID, "addElement")

#clicar 10x no elemento addElement
for _ in range(10):
    btnAddElement.click() #clica em um link

#captura vários elementos da tag input (captura vários elementos)
btnInputsChecker = browser.find_elements(By.TAG_NAME, "input")

#btnInputsChecker retorna uma lista, então tem que iterar sobre cada elemento para manipulá-los
for checker in btnInputsChecker:
    checker.click() #seleciona um checkbox

#espera 5s para encerrar a execução do código
time.sleep(5)
#fechar janela do navegador
browser.quit()