from behave import given, when, then
#from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


@given(u'que estou na página deo Instituto Joga Junto')
def step_on_instituto_page(context):
    
    title = context.browser.title
    assert 'Instituto Joga Junto' in title, 'Título não encontrado'


@when(u'preencho o formulário de contato')
def step_fill_form(context):
    context.browser.find_element(By.NAME, 'email').send_keys('emailtest@test')
    context.browser.find_element(By.NAME, 'nome').send_keys('Tamires Pereira')
    context.browser.find_element(By.NAME, 'body').send_keys('Minha automação com behave')

    select_subjects = context.browser.find_element(By.NAME, 'assunto')

    select = Select(select_subjects)

    select.select_by_visible_text('Ser facilitador')


@when(u'aperto o botão de enviar')
def step_send(context):
    context.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button").submit()


@then(u'os dados são recebidos com sucesso')
def step_impl(context):
    #import ipdb;ipdb.sset_trace()
    wait = WebDriverWait(context.browser, 10)
    alert = wait.until(EC.alert_is_present())
    

    assert 'Dados recebidos!' in alert.text(), 'Dados não foram recebidos!'
    
    