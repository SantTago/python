from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome() # para abrir o .Chrome
navegador.get('https://www.youtube.com/watch?v=kCazaXjQGuw') # comando .get para ir pra um pagina
time.sleep(50)
navegador.find_element(By.XPATH,'//*[@id="Form1"]/header/div/div/div/div[2]/ul/li[3]/a').click # click para clicar # para encontrar o elemento Copia o xpath


        
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located



with webdriver.Chrome() as driver:

    driver.get("http://google.com")
    wait = WebDriverWait(driver, 10)
    
    #driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    
    wait.until(presence_of_element_located((By.XPATH, '//*[@id="rcnt"]')))
    results = driver.find_elements(By.XPATH, "//a[@href]")

    for i, elem in enumerate(results):
        print(f'#{i} {elem.text} ({elem.get_attribute("href")})')