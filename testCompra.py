from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from seleniumbase import SB
import time

GMAIL = 'ttcomentador'
PASSWORD = 'wendel17'
CPF = "99999999999"
CEP = "59010015"
    

with SB(uc=True, headed=True) as driver:
    driver.get("http://localhost:8000/")
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
    user_name = driver.find_element(By.ID, "user_name").text
    assert user_name == "COMENTADOR TT"
    
    minhas_compras = driver.find_element(By.ID, "minhas_compras")
    minhas_compras.click()
    time.sleep(2)
    if(driver.is_element_present(By.ID, "deletar_compra")):
        driver.find_element(By.ID, "deletar_compra").click() 
    
    driver.save_screenshot("PaginaInicial.png")
    elemento_desejado = driver.find_element(By.ID, "pricing")
    driver.execute_script("arguments[0].scrollIntoView();", elemento_desejado)                                        
    time.sleep(2)                                            
    driver.save_screenshot("PacoteBasico.png")                                        

    escolher_plano_basico_button = driver.find_element(By.ID, "CompraBasico")
    escolher_plano_basico_button.click()
    time.sleep(2)
    if(driver.is_element_present(By.ID,"atualizarDados")):
        cep_user = driver.find_element(By.ID, "cepUsuario")
        cep_user.send_keys(CEP)
    
        cpf_user = driver.find_element(By.ID, "cpfUsuario")
        cpf_user.send_keys(CPF)
        
    
        button_submit = driver.find_element(By.ID, "confirmaDados")
        button_submit.click() 
        time.sleep(2)
    
        elemento_desejado = driver.find_element(By.ID, "pricing")
        driver.execute_script("arguments[0].scrollIntoView();", elemento_desejado)                                        
        time.sleep(2) 
        escolher_plano_basico_button = driver.find_element(By.ID, "CompraBasico")
        escolher_plano_basico_button.click()
        number_user = driver.find_element(By.ID, "numero_casa")
        number_user.send_keys("123")

    elemento_compra = driver.find_element(By.ID, "numero_casa")
    driver.execute_script("arguments[0].scrollIntoView();", elemento_compra)
    if not elemento_compra.get_attribute('value'):
        elemento_compra.send_keys("123")
    finalizar_compra_basico = driver.find_element(By.ID, "finalizarCompraBasico")
    finalizar_compra_basico.click()
    
    time.sleep(5) 

    driver.assert_element(By.ID,"success")
    minhas_compras = driver.find_element(By.ID, "minhas_compras")
    minhas_compras.click()
    time.sleep(2) 
    tableMinhasCompras = driver.find_element(By.ID, "tableMinhasCompras").text 
    assert "basico" in tableMinhasCompras
    driver.save_screenshot("compraResult.png")
