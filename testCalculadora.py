from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import SB
import time

with SB(uc=True, headed=True) as driver:
    driver.maximize_window()
    driver.get("http://localhost:8000/")

    elemento_desejado = driver.find_element(By.ID, "simulacao")
    driver.execute_script("arguments[0].scrollIntoView();", elemento_desejado)
    time.sleep(2)

    input_calc = driver.find_element(By.ID, "quantidadeAdicional")
    input_calc.send_keys(0)
    
    input2_calc = driver.find_element(By.ID, "consumoMedio")
    input2_calc.send_keys(360)

    texto_esperado = "A produção é igual à demanda, seus custos serão zerados."

    button_calc = driver.find_element(By.ID, "enviarEconomy")
    button_calc.click()
    
    time.sleep(2)
    driver.save_screenshot("CalculadoraResultado.png")

    resultado = driver.find_element(By.ID, "economyOutput").text
    driver.save_screenshot("CalculadoraResultado2.png")
    assert resultado == texto_esperado

    
    