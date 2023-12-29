from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from seleniumbase import SB
import time

GMAIL = 'ttcomentador'
PASSWORD = 'wendel17'
    

with SB(uc=True, headed=True) as driver:
    driver.maximize_window()
    driver.get("http://localhost:5500/")
    time.sleep(2)

    google_link = driver.find_element(By.ID, "login")
    google_link.click()

    identifier_field = driver.find_element(By.NAME, "identifier")
    identifier_field.send_keys(GMAIL)

    driver.save_screenshot("Google.png")

    avancar_button = driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button")
    avancar_button.click()


    time.sleep(2)


    passwd_field = driver.find_element(By.NAME, "Passwd")
    passwd_field.send_keys(PASSWORD)

  
    driver.save_screenshot("Google2.png")

   
    avancar_pwd = driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button")
    avancar_pwd.click()
    time.sleep(2)
    driver.save_screenshot("PaginaInicialDashboard.png")
    menu = driver.find_element(By.ID, "menu")
    menu.click()
    financeiro = driver.find_element(By.ID, "financeiro")
    financeiro.click()
    despesas = driver.find_element(By.ID, "despesas")
    despesas.click()
    criarDespesa = driver.find_element(By.ID, "criarDespesa")
    criarDespesa.click()
    descricao = driver.find_element(By.ID, "descricao")
    descricao.send_keys("Transporte de Placas Solares")
    categoria = driver.find_element(By.ID, "categoria")
    select = Select(categoria)
    opcao_desejada = "Transporte"
    select.select_by_visible_text(opcao_desejada)
    valor = driver.find_element(By.ID, "valor")
    valor.send_keys(1000)
    data = driver.find_element(By.ID, "data_despesa")
    data.send_keys("21/12/2023")
    driver.find_element(By.ID, "salvarDespesa").click()
    texto_esperado = "Descrição: Transporte de Placas Solares"
    resultado = driver.find_element(By.ID, "desc_despesa").text
    driver.save_screenshot("CalculadoraResultado2.png")
    time.sleep(2)
    assert resultado == texto_esperado

    driver.save_screenshot("DespesaFinal.png")
