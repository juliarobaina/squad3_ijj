from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select

browser = Firefox()

link = "https://www.google.com"

browser.get(link)

input_area = browser.find_element(By.NAME, "q")
input_area.send_keys("Instituto Joga Junto")
input_area.send_keys(Keys.ENTER)

sleep(3)

results_search = browser.find_elements(By.TAG_NAME, "h3")

check = False

if results_search:
    for result in results_search:
        if "Instituto Joga Junto" in result.text:
            result.click()
            print("AEEEEEEEEEEE")
            break

sleep(4)

assert "Instituto Joga Junto" in browser.title

#envio de dados para o formulário

field_name = browser.find_element(By.NAME, "nome").send_keys("Tamires Ana")

field_email = browser.find_element(By.NAME, "email").send_keys("tamires@email.com")

field_message = browser.find_element(By.NAME, "body").send_keys("Minha primeira automação com Selenium")

field_subject = browser.find_element(By.NAME, "assunto")

select_subject = Select(field_subject)

select_subject.select_by_visible_text("Ser facilitador")

btn_send = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button").submit()

browser.quit()







